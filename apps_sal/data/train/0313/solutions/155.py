class Solution:
    def minDays(self, bd: List[int], no_of_bouqs: int, flowers_in_a_bouq: int) -> int:
        if len(bd) < no_of_bouqs * flowers_in_a_bouq:
            return -1

        def condition(minDays):
            #print(minDays,end=' ')
            bouq = 0
            bouq_flowers = 0
            for i in bd:
                if i <= minDays:  # The flower can be used
                    bouq_flowers += 1
                    if bouq_flowers == flowers_in_a_bouq:
                        bouq += 1
                        bouq_flowers = 0
                        if bouq == no_of_bouqs:
                            return True
                if i > minDays:
                    bouq_flowers = 0
                # print(i,minDays,bouq_flowers,bouq)
            return False

        l = min(bd)
        r = max(bd)
        while l < r:
            mid = (l + r) // 2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
        return l
