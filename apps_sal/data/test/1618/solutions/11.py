n = int(input())
a = list(map(int, input().split()))
m = int(input())
l = [list(map(int, input().split())) for _ in range(m)]
ans = [a[l[0][0] - 1]]
lasth = l[0][1]
for (_, [w, h]) in enumerate(l[1:]):
    ans.append(max(ans[-1] + lasth, a[w - 1]))
    lasth = h
print(*ans, sep='\n')
