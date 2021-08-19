class DSet:

    def __init__(self, n):
        self.parents = [-1 for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, n):
        if self.parents[n] is -1:
            return n
        ret = self.find(self.parents[n])
        self.parents[n] = ret
        return ret

    def union(self, a, b):
        if a is -1 or b is -1:
            return False
        (x, y) = (self.find(a), self.find(b))
        if self.find(a) == self.find(b) and x is not -1:
            return False
        if self.rank[x] == self.rank[y]:
            self.parents[x] = y
            self.rank[x] = self.rank[y] = self.rank[x] + 1
        elif self.rank[x] > self.rank[y]:
            self.parents[y] = x
            self.rank[y] = self.rank[x]
        else:
            self.parents[x] = y
            self.rank[x] = self.rank[y]
        return True


ds = DSet(2 * int(input()))
(str1, str2) = (input(), input())
alphaHash = [-1 for i in range(26)]
for i in range(len(str1)):
    ds.union(i, alphaHash[ord(str1[i]) - ord('a')])
    alphaHash[ord(str1[i]) - ord('a')] = i
    ds.union(len(str1) + i, alphaHash[ord(str2[i]) - ord('a')])
    alphaHash[ord(str2[i]) - ord('a')] = len(str1) + i
ans = []
for i in range(len(str1)):
    if ds.union(i, len(str1) + i):
        ans.append((str1[i], str2[i]))
print(len(ans))
for x in ans:
    print(x[0] + ' ' + x[1])
