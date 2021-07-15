N, A, B = map(int, input().split())
d = N//(A+B)
ans = 0
ans += A*d
ans += min(N - (A+B)*d, A)
print(ans)
