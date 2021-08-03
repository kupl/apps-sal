c = [int(x) for x in input().split()]
n, m = list(map(int, input().split()))
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
bu = min(c[2], sum(min(c[1], c[0] * ai) for ai in a))
tr = min(c[2], sum(min(c[1], c[0] * bi) for bi in b))
print(min(c[3], bu + tr))
