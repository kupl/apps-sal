n = int(input())
a = list(map(int, input().split()))

limak = a[0]
a = a[1:]

c = [0] * (1001)
for votes in a:
    c[votes] += 1

ans = 0
cur_max = max(a)
while limak <= cur_max:
    limak += 1
    ans += 1
    c[cur_max] -= 1
    c[cur_max - 1] += 1
    if c[cur_max] == 0:
        cur_max -= 1

print(ans)
