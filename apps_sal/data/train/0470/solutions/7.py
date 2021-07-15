class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        count = collections.Counter(A)
        valuelist = list(count.keys())
        valuelist.sort()
        res = 0
        for i in range(len(valuelist)):
            for j in range(i, len(valuelist)):
                a = valuelist[i]
                b = valuelist[j]
                c = target - a - b
                if c not in count:
                    continue
                if a == b == c:
                    res += count[a] * (count[a] - 1) * (count[a] - 2) // 6 #C x 3
                elif a == b and b != c:
                    res += count[a] * (count[a] - 1) // 2 * count[c]
                elif a < b and b < c:
                    res += count[a] * count[b] * count[c]
        return res % (10 ** 9 + 7)
