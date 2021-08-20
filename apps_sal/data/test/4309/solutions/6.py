n = int(input())
(q, mod) = divmod(n, 111)
if mod == 0:
    print(q * 111)
else:
    print((q + 1) * 111)
