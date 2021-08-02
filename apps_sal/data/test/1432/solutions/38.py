N = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(N)]

sign = 1
for a in A:
    ans[0] += sign * a
    sign *= -1


for i in range(1, N):
    ans[i] = 2 * A[i - 1] - ans[i - 1]

print((*ans))

"""
ダム1: 2( a1 - a2 + a3 )
ダム2: 2( a2 - a3 + a1 )
ダム3: 2( a3 - a1 + a2 )
"""
