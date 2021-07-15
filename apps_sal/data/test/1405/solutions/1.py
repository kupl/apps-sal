import sys
sys.setrecursionlimit(10000)
n = int(input())
a = list(map(int, input().split()))

# sa = dict(zip(a, range(n)))
sb = {}
for num in a:
    if not num in sb:
        sb[num]=1
    else:
        sb[num]+=1

def go(a, b):
    ans = 0
    ab = a+b
    if ab in sb and sb[ab]>0:
        sb[ab]-=1
        ans = 1 + go(b, ab)
        sb[ab]+=1
    return ans

maxans = 2
for a in sb:
    for b in sb:
        if a!=b or sb[a]>1:
            count = 2
            sb[a] -= 1
            sb[b] -= 1
            count += go(a,b)
            sb[a] += 1
            sb[b] += 1
            if count > maxans:
                maxans = count
print(maxans)
