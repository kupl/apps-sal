n = int(input())
a = list(map(int, input().split()))
alice = 0
bob = 0
a.sort(reverse=True)
for i in range(0, n, 2):
    alice += a[i]
for i in range(1, n, 2):
    bob += a[i]
print(alice - bob)
