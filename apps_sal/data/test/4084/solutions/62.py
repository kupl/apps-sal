(N, A, B) = map(int, input().split())
ans = N // (A + B) * A
nokori = N % (A + B)
ans += min(A, nokori)
print(ans)
