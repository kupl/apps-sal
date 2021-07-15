n = int(input())
w = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(n-i-1):
        if w[i] == w[-j-1]:
            print('No')
            return

for i in range(n):
    if i < n-1:
        if w[i][-1] != w[i+1][0]:
            print('No')
            return

print('Yes')
