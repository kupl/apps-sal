class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        bloom_day_flowers = {}
        for i, day in enumerate(bloomDay):
            bloom_day_flowers.setdefault(day, []).append(i)

        days = sorted(bloom_day_flowers.keys())

        segments = {}
        total_b = 0

        for day in days:
            for flower in bloom_day_flowers[day]:
                assert flower not in segments

                lower_ext, upper_ext = False, False
                lower_rm, upper_rm = 0, 0
                new_seg = None

                # check lower interval
                if flower - 1 in segments:
                    seg = segments[flower - 1]
                    seg[1] = flower
                    segments[flower] = seg
                    lower_rm = seg[1] - seg[0]
                    if lower_rm > 1:
                        del segments[flower - 1]
                    new_seg = seg
                    lower_ext = True

                # check upper interval
                if flower + 1 in segments:
                    if flower in segments:
                        # merge segments
                        lower_seg = segments[flower]
                        upper_seg = segments[flower + 1]
                        upper_rm = upper_seg[1] - upper_seg[0] + 1

                        new_end = upper_seg[1]
                        lower_seg[1] = new_end
                        del segments[flower + 1]
                        del segments[flower]
                        segments[new_end] = lower_seg
                        new_set = lower_seg
                    else:
                        seg = segments[flower + 1]
                        seg[0] = flower
                        segments[flower] = seg
                        upper_rm = seg[1] - seg[0]
                        if upper_rm > 1:
                            del segments[flower + 1]
                        new_seg = seg
                    upper_ext = True

                if not (lower_ext or upper_ext):
                    seg = [flower, flower]
                    segments[flower] = seg
                    new_seg = seg

                total_b -= lower_rm // k + upper_rm // k
                total_b += (new_seg[1] - new_seg[0] + 1) // k

                # print(day, total_b, segments)
                if total_b >= m:
                    return day

        return -1
