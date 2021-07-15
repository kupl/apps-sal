import sys

n = int(input())
p = list(map(int,input().split()))
min = sys.maxsize
cnt = 0

for i in range(n):
    if min >= p[i]:
        min = p[i]
        cnt += 1

print(cnt)
