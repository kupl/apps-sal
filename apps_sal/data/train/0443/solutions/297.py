class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            l = [rating[i]]
            for j in range(i + 1, len(rating)):
                l.append(rating[j])
                for k in range(j + 1, len(rating)):
                    l.append(rating[k])
                    if (l[0] > l[1] and l[1] > l[2]) or (l[0] < l[1] and l[1] < l[2]):
                        count += 1
                    l = l[:2]
                l = l[:1]
        return count
