import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    flag = 0
    for i in range(2, int(n**.5) + 1):
        if(n % i == 0):
            print(n // i, (i - 1) * n // i)
            flag = 1
            break
    if(flag == 0):
        print(n - 1, 1)
