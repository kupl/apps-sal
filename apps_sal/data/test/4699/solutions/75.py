from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
D = set(map(int, input().split()))

while True:
    tmp = set(str(N))
    b = True
    for x in tmp:
        if int(x) in D:
            b = False
            break 
    if b == True:
        break
    else:
        N += 1

print(N)
