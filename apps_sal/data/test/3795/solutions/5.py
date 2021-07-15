n = int(input())    
d = int(input())
e = int(input())
e *= 5
res = n
for i in range((n // e) + 1):
    res = min(res, (n - i * e) % d)
print(res)
