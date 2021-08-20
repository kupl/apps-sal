n = int(str(input()).strip())
a = sorted([int(x) for x in str(input()).split(' ')])
md = min([abs(a1 - a0) for (a0, a1) in zip(a, a[1:])])
print(md, sum([md == abs(a1 - a0) for (a0, a1) in zip(a, a[1:])]))
