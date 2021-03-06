class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        d = {}
        for num in arr:
            rem = num % k
            if rem in d:
                d[rem].append(num)
            else:
                d[rem] = [num]
        print(d)
        for i in d:
            if i == 0 or (k % 2 == 0 and i == k // 2):
                if len(d[i]) % 2 != 0:
                    return False
            elif k - i in d:
                if len(d[i]) != len(d[k - i]):
                    return False
            else:
                return False
        return True
