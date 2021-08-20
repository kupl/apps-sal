class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        p = {}
        for i in range(lo, hi + 1):
            temp = 0
            copy_i = i
            if copy_i == 1:
                p[i] = 0
            while copy_i != 1:
                if copy_i % 2 == 0:
                    copy_i /= 2
                    temp += 1
                    if copy_i == 1:
                        p[i] = temp
                        break
                if copy_i % 2 != 0:
                    copy_i = 3 * copy_i + 1
                    temp += 1
                    if copy_i == 1:
                        p[i] = temp
                        break
        print('p is')
        print(p)
        p = sorted(list(p.items()), key=lambda x: x[1])
        track = 0
        for ele in p:
            track += 1
            if track == k:
                return ele[0]
