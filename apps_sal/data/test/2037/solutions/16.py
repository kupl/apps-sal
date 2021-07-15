n,m = map(int,input().split())

a = list(map(int,input().split()))

s = 0
b = [0]*(n+1)

for i in a:
    if b[i] == 0:
        s += 1
    b[ i ] += 1
    if s == n:
        print(1,end="")
        for i in range(n):
            b[i+1] -= 1
            if b[i+1] == 0:
                s -= 1
    else:
        print(0,end="")

