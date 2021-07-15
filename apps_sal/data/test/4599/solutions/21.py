n = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)
alice = 0
bob = 0
for i in range(len(a)):
    if i%2==0:
        alice += a[i]
    if i%2==1:
        bob += a[i]
print(alice-bob)
