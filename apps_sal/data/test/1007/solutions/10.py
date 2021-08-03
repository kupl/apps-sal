k, p = [int(x) for x in input().split()]

s = 0

for i in range(k):
    n = str(i + 1)
    n += n[::-1]
    s = (s + int(n)) % p

print(s)
