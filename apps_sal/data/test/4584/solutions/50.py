import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

ans = [0] * N
for a_i in A:
    ans[a_i-1] += 1

for a in ans:
    print(a)
