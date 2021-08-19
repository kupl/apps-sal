import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
S = set([0])
cnt = 0
ans = 0
for a in A:
    cnt += a
    if cnt in S:
        ans += 1
        S = set([0, a])
        cnt = a
    else:
        S.add(cnt)
print(ans)
