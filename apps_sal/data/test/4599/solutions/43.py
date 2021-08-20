n = int(input())
lst = list(map(int, input().split()))
alice = 0
bob = 0
lst.sort()
for i in range(n):
    if i % 2 == 0:
        alice += lst.pop()
    else:
        bob += lst.pop()
print(alice - bob)
