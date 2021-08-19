import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = [[a, i] for (i, a) in enumerate(A)]
B.sort(reverse=True)
ANS = 0
ind = 0
for (b, i) in B:
    ANS += b * ind + 1
    ind += 1
print(ANS)
print(*[B[i][1] + 1 for i in range(n)])
