class Solution:

    def minSetSize(self, a: List[int]) -> int:
        d = {}
        n = len(a) // 2
        for i in a:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(d)
        sum = 0
        count = 0
        for i in d:
            x = i[1]
            sum += x
            count += 1
            if sum >= n:
                break
        return count
