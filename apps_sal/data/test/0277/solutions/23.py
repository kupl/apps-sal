(n, a, b) = [int(x) for x in input().split()]
a -= 1
b -= 1
res = 0
while a != b:
    a //= 2
    b //= 2
    res += 1
if 2 ** res == n:
    print('Final!')
else:
    print(res)
