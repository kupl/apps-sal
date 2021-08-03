class Solution:
    def numTriplets(self, num1: List[int], num2: List[int]) -> int:
        dic1 = {}
        for i in range(len(num1)):
            for j in range(i + 1, len(num1)):
                if num1[i] * num1[j] in dic1:
                    dic1[num1[i] * num1[j]] += 1
                else:
                    dic1[num1[i] * num1[j]] = 1
        dic2 = {}
        for i in range(len(num2)):
            for j in range(i + 1, len(num2)):
                if num2[i] * num2[j] in dic2:
                    dic2[num2[i] * num2[j]] += 1
                else:
                    dic2[num2[i] * num2[j]] = 1
        ans = 0
        for i in num1:
            if i * i in dic2:
                ans += dic2[i * i]
        for i in num2:
            if i * i in dic1:
                ans += dic1[i * i]
        return ans
