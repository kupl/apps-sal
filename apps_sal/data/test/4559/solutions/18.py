n = int(input())
aaa = sorted(map(int, input().split()))
ans = 1
limit = 10 ** 18
for a in aaa:
    ans *= a
    if ans > limit:
        ans = -1
        break
print(ans)
