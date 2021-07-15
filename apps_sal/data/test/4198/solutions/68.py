a, b, x = map(int, input().split())

minNumber, maxNumber = 0, 10**9+1
answer = 0
while(minNumber+1 < maxNumber):
    n = (minNumber+maxNumber)//2
    if a*n + b*len(str(n)) > x:
        maxNumber = n
    else:
        minNumber = n

print(minNumber)
