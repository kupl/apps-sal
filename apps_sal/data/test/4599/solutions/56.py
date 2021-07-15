N = int(input())
a = list(map(int,input().split()))
a.sort()
a.reverse()
alice = 0
bob = 0
for i in range(N) :
    if i%2 == 0 : 
        alice += a[i]
    elif i%2 == 1 :
        bob += a[i]
print((alice-bob))

