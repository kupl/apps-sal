class Union_Find():
    def __init__(self, value):
        self.parents = None
        self.value = None

    def find_parents(self):
        if (self.parents == None):
            return self
        else:
            self.parents = self.parents.find_parents()
            return self.parents


n = int(input().strip())
s1 = input().strip()
s2 = input().strip()

dp = dict()
for i in s1:
    if i not in dp:
        dp[i] = Union_Find(i)
for i, v in enumerate(s2):
    if v not in dp:
        dp[v] = Union_Find(v)
    fr = dp[v].find_parents()
    to = dp[s1[i]].find_parents()
    if (fr != to):
        fr.parents = to

ans = dict()
cnt = 0
for i in dp:
    now = dp[i].find_parents()
    if now in ans:
        ans[now].append(i)
        cnt += 1
    else:
        ans[now] = [i]
print(cnt)
for i in ans:
    for j in range(1, len(ans[i])):
        print(ans[i][j - 1], ans[i][j])
