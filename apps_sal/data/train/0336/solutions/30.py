class Solution:

    def minSteps(self, a: str, b: str) -> int:
        count = 0
        dic1 = Counter(a)
        for i in b:
            if i in dic1:
                if dic1[i]:
                    dic1[i] -= 1
                else:
                    count += 1
            else:
                count += 1
        return count
