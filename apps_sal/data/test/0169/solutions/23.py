n = int(input())
a = int(input())
b = int(input())
c = int(input())


res = (n - b) // (b - c) + 1
if res >= 0:
    res += ((n - b) % (b - c) + c) // a

if res < n // a:
    res = n // a
print(res)
