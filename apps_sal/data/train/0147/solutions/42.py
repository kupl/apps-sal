class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        sorting = sorted([(s, i) for i, s in enumerate(speed)])
        speedset = set(i for _, i in sorting[len(sorting) - k:])
        ssum = sum(s for s, _ in sorting[len(sorting) - k:])
        removed = set()
        idx = len(sorting) - k

        ans = 0
        for e, i in sorted([(e, i) for i, e in enumerate(efficiency)]):
            if i in speedset:
                ans = max(ans, e * ssum)

                speedset.remove(i)
                ssum -= speed[i]

                idx -= 1
                while idx >= 0 and sorting[idx][1] in removed:
                    idx -= 1

                if idx >= 0:
                    speedset.add(sorting[idx][1])
                    ssum += sorting[idx][0]
            else:
                ans = max(ans, e * (ssum - sorting[idx][0] + speed[i]))
            removed.add(i)
        return ans % (10**9 + 7)
