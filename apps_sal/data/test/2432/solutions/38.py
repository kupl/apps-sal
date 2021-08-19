"""
2 = 2^1
24 = 2^3*3^1
50 = 2^1*5^2

2 = 10
5 = 101, 24 = 11000
35 = 100011, 50 = 110010

And after happily lived ever they
and they lived happily ever after

123456
164352

2 = 000010
2 = 000010

 5 = 000101
24 = 011000

35 = 100011
50 = 110010
"""
replacement = [4, 1, 3, 2, 0, 5] + list(range(6, 64))
n = list('{:064b}'.format(int(input())))
n.reverse()
ans = list(n)
for i in range(64):
    ans[i] = n[replacement[i]]
ans.reverse()
print(int(''.join(ans), 2))
