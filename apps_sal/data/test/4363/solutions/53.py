# coding: utf-8
# Your code here!

k, s = map(int, input().split())

cnt = 0

for i in range(k+1):
    for j in range(k+1):
        if s-i-j <= k and s-i-j>=0:
            cnt += 1

print(cnt)
