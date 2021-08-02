n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
alice = 0
bob = 0
for i in range(0, n, 2):
    alice += a[i]
    if i == n - 1:
        break
    bob += a[i + 1]
print(alice - bob)
