MAX_N = 1000000000
N = int(input())
A = [int(x) for x in input().split()]
cnt = 0
min_n = MAX_N
ans = 0
for a in A:
    ans += abs(a)
    if a <= 0:
        cnt += 1
    min_n = min(min_n, abs(a))
if cnt % 2 == 0:
    print(ans)
else:
    print(ans - min_n * 2)
