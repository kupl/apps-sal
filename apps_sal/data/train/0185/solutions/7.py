class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:

        def Hash_Function(b):
            num = list(b)
            num.reverse()
            total = 0
            increment = 1
            for item in num:
                if item == '1':
                    total = total + increment
                    increment = increment * 2
                else:
                    increment = increment * 2
                    continue
            return total
        start = 0
        end = k
        buckets = []
        buckets = set(buckets)
        while end <= len(s):
            num = Hash_Function(s[start:end])
            buckets.add(num)
            start += 1
            end += 1
        if len(buckets) == 2 ** k:
            return True
        else:
            return False
