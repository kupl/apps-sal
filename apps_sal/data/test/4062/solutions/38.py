(a, b, c, d) = list(map(lambda x: int(x), input().split()))
ac = a * c
ad = a * d
bc = b * c
bd = b * d
ans = max([ac, ad, bc, bd])
print(ans)
