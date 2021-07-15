n, d = [int(v) for v in input().split()]
a = {int(v) for v in input().split()}

b1 = {v - d for v in a}
b2 = {v + d for v in a}
s = (b1 | b2) - a

s = {v for v in b1 | b2 if min(abs(v - vv) for vv in a) == d}

print(len(s))

