n = input()
l = len(n)
n = int(n)

res = 1000
for i in range(l - 2):
    c = n // (10 ** i)
    c %= 1000
    res = min(res, abs(c - 753))
    # print(i,c)
print(res)
