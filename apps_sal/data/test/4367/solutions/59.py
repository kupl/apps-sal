N, R = map(int, input().split())

if N <= 9:
    ans = R + (1000 - 100 * N)
else:
    ans = R
print(ans)
