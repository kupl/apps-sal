n = int(input())
d = int(input())
e = int(input())
mn = 99999999999
while n >= 0:
    res = n % d
    if res < mn:
        mn = res
    n = n - 5 * e
print(mn)
