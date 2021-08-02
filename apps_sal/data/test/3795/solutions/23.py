n = int(input(""))
d = int(input(""))
e = int(input(""))
e *= 5
ans = n
for i in range(0, n // d + 1):
    a = (n - d * i) % e
    if a < ans:
        ans = a
print(ans)
