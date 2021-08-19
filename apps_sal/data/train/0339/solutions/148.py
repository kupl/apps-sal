from collections import defaultdict


class Solution:

    def numTriplets(self, num1: List[int], num2: List[int]) -> int:
        d11 = defaultdict(list)
        d12 = defaultdict(list)
        for i in range(len(num1)):
            for j in range(i, len(num1)):
                if i == j:
                    d11[num1[i] ** 2].append(i)
                else:
                    d12[num1[i] * num1[j]].append((i, j))
        d21 = defaultdict(list)
        d22 = defaultdict(list)
        for i in range(len(num2)):
            for j in range(i, len(num2)):
                if i == j:
                    d21[num2[i] ** 2].append(i)
                else:
                    d22[num2[i] * num2[j]].append((i, j))
        ans = 0
        for key in d11:
            if key in d22:
                ans += len(d11[key]) * len(d22[key])
        for key in d21:
            if key in d12:
                ans += len(d21[key]) * len(d12[key])
        return ans
