def read(): return list(map(int, input().split()))


n = int(input())

p = list(read())

b = list(read())

ans = (b.count(1) + 1) % 2

was = [0] * n

cnt = 0

for i in range(n):

    if not was[i]:

        cnt += 1

        v = i

        while not was[v]:

            was[v] = 1

            v = p[v] - 1

if cnt > 1:
    ans += cnt

print(ans)
