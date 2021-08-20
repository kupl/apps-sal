n = int(input())
a = [int(x) for x in input().split()]
zeroCount = 0
negCount = 0
ans = 0
for i in range(n):
    if a[i] == 0:
        zeroCount = zeroCount + 1
        ans += 1
    elif a[i] < 0:
        negCount = negCount + 1
        ans += -1 - a[i]
    else:
        ans += a[i] - 1
if zeroCount > 0 or negCount % 2 == 0:
    print(ans)
else:
    ans = ans + 2
    print(ans)
