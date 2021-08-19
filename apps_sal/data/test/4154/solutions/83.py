from itertools import accumulate
N, M = list(map(int, input().split()))

# left = 1
# right = N
#
# for i in range(M):
#     a,b = map(int, input().split())
#     left = max(left,a)
#     right = min(right, b)
#
# print(max(0,right-left+1))

imos = [0] * (N + 2)
for i in range(M):
    l, r = list(map(int, input().split()))
    imos[l] += 1
    imos[r + 1] -= 1

imos = list(accumulate(imos))

ans = 0
for im in imos:
    ans += (im == M)

print(ans)
