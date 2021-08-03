N = int(input())
A = list(map(int, input().split()))

ans = max(A) - min(A)

print(ans)
