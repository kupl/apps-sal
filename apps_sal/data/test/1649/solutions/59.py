(a, b, c, d) = map(int, input().split())
cand = [a + b, b + c, c + d, d + a, a + c, b + d, a, b, c, d]
s = sum([a, b, c, d])
if s % 2 == 1:
    print('No')
elif s // 2 in cand:
    print('Yes')
else:
    print('No')
