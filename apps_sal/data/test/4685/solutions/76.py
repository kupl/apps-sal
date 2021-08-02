A = list(map(int, input().split()))
K = int(input())

ans = sum(A)
ans += max(A) * (2**K - 1)
print(ans)
