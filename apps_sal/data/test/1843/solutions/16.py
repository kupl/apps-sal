def log2(n):
    i = 1
    while i <= n:
        i *= 2
    return i

t = int(input())
for i in range(t):
    n = int(input())
    print(n*(n+1)//2 - 2*(log2(n)-1))

