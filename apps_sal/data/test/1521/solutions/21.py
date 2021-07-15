import sys
p,n = list(map(int,input().split()))
a = [0] * p;
for i in range(n):
    x = int(input())
    if (a[x % p] != 0):
        print(i + 1)
        return
    else:
        a[x % p] = i + 1;
print(-1)

