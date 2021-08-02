import sys
n = int(input())
a = list(map(int, input().split()))

if a.count(0) > 0:
    print("0")
    return

ans = 1
for i in range(n):
    ans *= a[i]
    if ans > 10 ** 18:
        print("-1")
        return

print(ans)
