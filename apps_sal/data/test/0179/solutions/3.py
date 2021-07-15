from math import factorial
mod = 1000000007

n, x, pos = list(map(int, input().split()))
biggerNeeded = 0
lowerNeeded = 0
left = 0
right = n
while left < right:
    #print(left, right)
    middle = (left+right)//2
    if middle < pos:
        left = middle + 1
        lowerNeeded += 1
    elif middle > pos:
        right = middle
        biggerNeeded += 1
    else:
        left = middle + 1
if x+biggerNeeded > n or x-lowerNeeded <= 0:
    print(0)
    return
ans = factorial(x-1) // factorial(x-1-lowerNeeded)
ans %= mod
ans *= factorial(n-x) // factorial(n-x-biggerNeeded)
ans %= mod
ans *= factorial(n-biggerNeeded-lowerNeeded-1)
ans %= mod
print(ans)

