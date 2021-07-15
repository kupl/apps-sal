n, m, c = map(int, input().split())

b = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    a = [int(x) for x in input().split()]
    cnt = c
    for aa, bb in zip(a, b):
        cnt += aa * bb
    if cnt > 0: ans += 1
print(ans)
