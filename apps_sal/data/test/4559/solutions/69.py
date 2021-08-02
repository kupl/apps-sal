import sys

n = int(input())
li = list(map(int, input().split()))
ans = 1

if 0 in li:
    print(0)
    return

for i in range(n):
    ans = ans * li[i]
    if ans > 10**18:
        print(-1)
        return

print(ans)
