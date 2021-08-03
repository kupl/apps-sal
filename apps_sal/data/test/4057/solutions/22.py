t = int(input())
l = [int(x) for x in input().split()]
s = set(l)
p = [l.count(i) for i in s]
print(max(p))
