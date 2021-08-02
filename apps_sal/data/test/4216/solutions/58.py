n = int(input())
i = 1
a = []
while i**2 <= n:
    if n % i == 0:
        b = [str(i), str(n // i)]
        a.append(b)
    i += 1
print(len(a[-1][1]))
