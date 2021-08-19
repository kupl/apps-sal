class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = {}
        l = []
        for i in range(lo, hi + 1):
            j = i
            stack = []
            stack.append(j)
            if j not in powers:
                while j != 1:
                    if j % 2 == 0:
                        j = j // 2
                        stack.append(j)
                    else:
                        j = j * 3 + 1
                        stack.append(j)
                cnt = 0
                while stack:
                    j = stack.pop()
                    powers[j] = cnt
                    cnt += 1
            l.append((i, powers[i]))
        l = sorted(l, key=lambda x: (x[1], x[0]))
        return l[k - 1][0]
