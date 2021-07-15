N = int(input())
v = [int(i) for i in input().split()]
w = sorted(v)

ans = w[0] + w[1]
if N == 2:
    ans /= 2
else:
    for i in range(2, N):
        ans += 2**(i-1) * w[i]
    ans /= 2**(N-1)

print(ans)
