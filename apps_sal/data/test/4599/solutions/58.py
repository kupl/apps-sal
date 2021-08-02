n = int(input())
a = list(map(int, input().split()))
alice = 0
bob = 0

a_sort = sorted(a, reverse=True)

for i in range(n):
    if i % 2 == 0:
        alice += a_sort[i]
    else:
        bob += a_sort[i]

print(alice - bob)
