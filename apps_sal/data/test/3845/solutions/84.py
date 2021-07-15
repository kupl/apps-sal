"""
感想

- 最大ケースでビッシリつめて市松模様にしないといけないかと思った
-
"""
A, B = list(map(int, input().split()))
M = [['.']*100 for _ in range(50)] + [['#']*100 for _ in range(50)]
A -= 1
B -= 1
for i in range(B):
    i *= 2
    M[(i//50)*2][i%50] = '#'

for i in range(A):
    i *= 2
    M[51+(i//50)*2][i%50] = '.'
print((100, 100))
for m in M:
    print((''.join(m)))

