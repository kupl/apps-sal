import sys

n = int(input())
a = list(map(int, input().split()))

cnt = [0] * n

while 1:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] /= 2
            cnt[i] += 1
        else:
            print(min(cnt))
            return
