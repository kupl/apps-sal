n = input()
leng = len(n)
a = n[0:leng // 2]
b = n[(leng + 3) // 2 - 1:]
if n == n[::-1] and a == a[::-1] and (b == b[::-1]):
    print('Yes')
else:
    print('No')
