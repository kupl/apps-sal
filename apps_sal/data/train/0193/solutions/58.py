from collections import Counter
class Solution:
    def minSetSize(self, arr) -> int:
        counterArr = [0] * (len(arr) + 1)
        for value in Counter(arr).values():
            counterArr[value] += 1
        steps = 0
        total = 0
        print(counterArr)
        for i in reversed(range(len(arr) + 1)):
            num = counterArr[i]
            for j in range(num):
                total += i
                steps += 1
                if total >= len(arr) // 2:
                    return steps
        return steps
