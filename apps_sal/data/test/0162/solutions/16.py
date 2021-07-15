n, k = list(map(int, input().split()))

ans = 10**18

for a in map(int, input().split()):
    if k % a == 0:
        ans = min(ans, k // a)

print(ans)

