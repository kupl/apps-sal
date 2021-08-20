(N, A, B) = list(map(int, input().split()))
ans = N // (A + B) * A
ans += min(N % (A + B), A)
print(ans)
