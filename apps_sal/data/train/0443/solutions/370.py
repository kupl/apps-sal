class Solution:

    def numTeams(self, rating: List[int]) -> int:
        less = {}
        more = {}
        count = []
        n = len(rating)
        for i in range(n):
            l = []
            m = []
            for j in range(i + 1, n):
                if rating[i] < rating[j]:
                    l.append(rating[j])
                if rating[i] > rating[j]:
                    m.append(rating[j])
            if len(l) > 0:
                less[rating[i]] = l
            if len(m) > 0:
                more[rating[i]] = m
        print((less, more))
        for i in list(less.keys()):
            t = less[i]
            for j in t:
                if j in list(less.keys()):
                    for k in less[j]:
                        count.append([i, j, k])
        for i in list(more.keys()):
            t = more[i]
            for j in t:
                if j in list(more.keys()):
                    for k in more[j]:
                        count.append([i, j, k])
        return len(count)
