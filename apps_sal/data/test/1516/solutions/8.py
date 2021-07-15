from collections import defaultdict
m = 998244353
n = int(input())


#a = list(map(int,input().split()))
a = list(input().split())
digits = defaultdict(int)

l = len(a[0])*2
for x in a:
    for i,c in enumerate(x):
        digits[l-i*2] += int(c)*n
        digits[l-i*2-1]+= int(c)*n

for x in range(1,l+1):
    current = digits[x]
    over = current//10
    digits[x+1]+=over
    digits[x]%=10

out = 0
mu = 1
for k in sorted(digits.keys()):
    out += digits[k]*mu
    out %= m
    mu *=10
print (out)
