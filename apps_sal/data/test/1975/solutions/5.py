n, m = map(int, input().split())
ii = set()
jj = set()

ans = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i not in ii or j not in jj:
            ans.append((i, j))
            ii.add(i)
            jj.add(j)
print(len(ans))
for a, b in ans:
    print(a, b)
