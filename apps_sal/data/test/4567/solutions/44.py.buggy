import sys
N = int(input())
s = [int(input()) for i in range(N)]
num = sum(s)

if num % 10 != 0:
    print(num)
else:
    for i in range(N):
        s = sorted(s)
        if s[i] % 10 == 0:
            continue
        else:
            print(num - s[i])
            return
    print(0)
