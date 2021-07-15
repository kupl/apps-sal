n = int(input())
a = [int(s) for s in input().split()]
a.sort(reverse=True)
alice = sum(a[0:n:2])
bob = sum(a[1:n:2])

print(alice - bob)
