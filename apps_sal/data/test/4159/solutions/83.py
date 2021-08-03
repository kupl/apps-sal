a, b, k = (int(x) for x in input().split())
c = a

if a + b <= k:
    a = 0
    b = 0
elif a <= k:
    a = 0
    b = b + c - k
elif a > k:
    a = a - k

c = str(a) + " " + str(b)
print(c)
