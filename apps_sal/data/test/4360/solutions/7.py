N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    if a == 0:
        continue
    ans += 1 / a
if ans == 0:
    print(0)
else:
    print(1 / ans)
