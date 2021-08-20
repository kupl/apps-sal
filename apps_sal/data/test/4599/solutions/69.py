N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
alice = 0
for i in range(0, N, 2):
    alice += a[i]
bob = sum(a) - alice
print(alice - bob)
