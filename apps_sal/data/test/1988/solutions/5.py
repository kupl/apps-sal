import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    tmp = a[0:]
    ans = -1
    for i in range(n):
        cnt = n - i
        if cnt % 2 == 0:
            if a[i:n] + a[0:i] < tmp:
                tmp = a[i:n] + a[0:i]
                ans = i
            
        else:
            if a[i:n] + a[0:i][::-1] < tmp:
                tmp = a[i:n] + a[0:i][::-1]
                ans = i
    print(tmp)
    print(ans + 1)

