input()
p = {(1 << 'RGBYW'.index(c)) + (1 << int(k) + 4) for c, k in input().split()}
print(min(bin(t).count('1') for t in range(1024) if len({t & q for q in p}) == len(p)))
