class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for i in range(len(rating)):
            fst = rating[i]
            for j in range(i + 1, len(rating)):
                scn = rating[j]
                if fst == scn:
                    break
                a = fst > scn
                for k in range(j + 1, len(rating)):
                    thr = rating[k]
                    if scn == thr:
                        break

                    if a and scn > thr:
                        cnt = cnt + 1

                    if not a and scn < thr:
                        cnt = cnt + 1

        return cnt
