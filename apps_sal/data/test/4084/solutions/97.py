N, A, B = list(map(int, input().split()))

ans = N // (A + B) * A
ans += min(A, N % (A + B))

print(ans)
