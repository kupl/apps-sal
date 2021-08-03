n = int(input())
data = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    k, pos = list(map(int, input().split()))
    s = data[:]
    ans = []
    for i in range(k):
        x = s.index(max(s))
        ans.append(x)
        s[x] = -1
    ans.sort()
    print(data[ans[pos - 1]])
