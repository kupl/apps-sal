N = int(input())
B = list(map(int, input().split()))
ans = B[0]
for i in range(1, len(B)):
    ans += min(B[i], B[i - 1])
ans += B[-1]
print(ans)
