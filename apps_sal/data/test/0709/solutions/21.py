n = int(input())
col = 0
while n > 0:
    q = 0
    while 2 ** (q + 1) <= n:
        q += 1
    n -= 2 ** q
    col += 1
print(col)
        

