n = int(input())
A = sorted(list(map(int, input().split())))
ans = 1
for a in A:
    ans *= a
    if ans > 10**18:
        ans = -1
        break
print(ans)
