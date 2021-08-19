N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    ans += 1 / a
ans = 1 / ans
print(ans)
