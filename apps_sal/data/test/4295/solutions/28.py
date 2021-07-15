N,K = map(int, input().split())

y = N%K
z = abs(K-y)

ans = min(y,z)

print(ans)
