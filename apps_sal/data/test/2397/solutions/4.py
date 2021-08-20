import sys
input = sys.stdin.readline
(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
SUM = [0]
for a in A[::-1]:
    SUM.append(SUM[-1] + a)
SUM = SUM[::-1]
ANS = SUM[0]
ANS += sum(sorted(SUM[1:-1], reverse=True)[:k - 1])
print(ANS)
