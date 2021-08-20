class Solution:

    def rankTeams(self, votes: List[str]) -> str:
        m = len(votes[0])
        n = len(votes)
        dic = {}
        for vote in votes:
            for i in range(m):
                if vote[i] not in dic:
                    dic[vote[i]] = [0] * m
                dic[vote[i]][i] += 1
        li = []
        for (k, v) in list(dic.items()):
            values = [str(n - i) for i in v]
            values.append(k)
            li.append(''.join(values))
        li.sort()
        return ''.join([item[-1] for item in li])
