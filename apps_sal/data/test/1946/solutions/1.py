n = int(input())
di = {}
for i in range(n):
    a, b = (list(map(int, input().strip().split(' '))))
    try:
        p = di[a]
        di[a] = max(di[a], b)
    except KeyError:
        di[a] = b
m = int(input())
for i in range(m):
    a, b = (list(map(int, input().strip().split(' '))))
    try:
        p = di[a]
        di[a] = max(di[a], b)
    except KeyError:
        di[a] = b
ans = 0
for i in di:
    ans += di[i]
print(ans)
