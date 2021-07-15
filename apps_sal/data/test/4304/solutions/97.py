A, B = map(int, input().split())
d = B-A
s = sum([x for x in range(1, d)])
print(s-A)
