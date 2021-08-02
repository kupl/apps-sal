N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N)]
A = sorted([a for a, b in AB])
B = sorted([b for a, b in AB])

ans = B[N // 2] + B[(N - 1) // 2] - (A[N // 2] + A[(N - 1) // 2])
if N % 2:
    ans //= 2
ans += 1
print(ans)
