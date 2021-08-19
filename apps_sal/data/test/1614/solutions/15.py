(n, h) = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
print(sum([1 if x <= h else 2 for x in A]))
