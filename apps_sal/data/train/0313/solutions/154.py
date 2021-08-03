class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        bloomDay_sort = sorted(bloomDay)
        bloomDay_dict = {}
        num = 0
        prev = -1
        for item in bloomDay_sort:      # 离散
            if item != prev:
                bloomDay_dict[num] = item
                num += 1
                prev = item

        # 二分day
        bloomDay_tmp = [0 for ii in range(len(bloomDay))]
        l, r = 0, num
        while l < r:
            mid = (l + r) // 2
            for i in range(len(bloomDay)):
                if bloomDay[i] <= bloomDay_dict[mid]:
                    bloomDay_tmp[i] = 1
                else:
                    bloomDay_tmp[i] = 0

            count_nonlocal = 0
            count = 0
            for i in range(len(bloomDay_tmp)):
                if bloomDay_tmp[i] == 1:
                    count += 1
                else:
                    count_nonlocal += count // k
                    count = 0

            if count != 0:
                count_nonlocal += count // k
                count = 0

            if count_nonlocal >= m:
                r = mid
            else:
                l = mid + 1

        return bloomDay_dict[l]      #
