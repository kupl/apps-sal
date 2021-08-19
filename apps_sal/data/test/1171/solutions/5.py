# 左から取り出すパターンは最大50通り
# 右から取り出すパターンは最大50通り
# その組み合わせは2500通り
# その全通りに対して、マイナスの石を引けるだけ引くパターンを試すと50
# 125000
# すべて試す

import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())
V = [0] + list(map(int, readline().split())) + [0]
N += 2
K += 2

leftsum = 0
leftminus = []
ans = -(10 ** 9)
for left in range(min(N, K)):
    leftsum += V[left]
    if V[left] < 0:
        leftminus += [V[left]]
    rightsum = 0
    rightminus = []
    limit = min(N - (left + 1), K - (left + 1))
    for right in range(N - 1, N - limit - 1, -1):
        rightsum += V[right]
        if V[right] < 0:
            rightminus += [V[right]]
        allsum = leftsum + rightsum
        rest = max(K - ((left + 1) + (N - right)), 0)
        allminus = sorted(leftminus + rightminus)
        allsum -= sum(allminus[:rest])
        if allsum > ans:
            ans = allsum
print(ans)
