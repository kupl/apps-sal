import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

from collections import defaultdict

N, M = list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

dic = defaultdict(int)
dic[0] += 1
ans = 0
for i in range(N):
    A[i + 1] += A[i]
    A[i + 1] %= M
    ans += dic[A[i + 1]]
    dic[A[i + 1]] += 1

print (ans)



