class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = {}
        zero_count = 0
        for num in A:
            if num == 0:
                zero_count += 1
            elif num in count:
                count[num] += 1
            else:
                count[num] = 1
        if zero_count % 2 != 0:
            return False

        A.sort()
        for num in A:
            double = num * 2
            if num in count and double in count:
                count[double] -= 1
                count[num] -= 1
                if count[double] == 0:
                    count.pop(double)
                if count[num] == 0:
                    count.pop(num)

        return count == {}
