class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        track = dict()
        for i in range(lo, hi + 1):
            power = 0
            x = i
            while i != 1:
                if i % 2 == 0:
                    i = i // 2
                else:
                    i = 3 * i + 1
                power += 1
            track[x] = power
        sorted_tr = sorted(track.items(), key=lambda x: [x[1], x[0]])
        print(sorted_tr)
        return sorted_tr[k - 1][0]
