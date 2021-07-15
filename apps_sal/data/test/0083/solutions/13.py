N = int(input())
A = [int(a) for a in input().split()]

pos = 0
neg = 0
for a in A:
    if a > 0:
        pos += 1
    elif a < 0:
        neg += 1
        
if pos >= (N+1)//2:
    print(1)
elif neg >= (N+1)//2:
    print(-1)
else:
    print(0)

