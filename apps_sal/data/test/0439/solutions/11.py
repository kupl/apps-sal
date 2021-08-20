n = int(input())
m = int(input())
if n >= 27:
    print(m)
else:
    k = m % (1 << n)
    print(k)
