def gcd(a, b): 
    if(b == 0): 
        return a 
    else: 
        return gcd(b, a % b) 

n = int(input())
a = list(map(int, input().split()))

maxa = max(a)

r = [maxa - x for x in a]

z = r[0]
for i in range(1, n):
    z = gcd(z, r[i])

y = sum(r) // z
print(y, z)

