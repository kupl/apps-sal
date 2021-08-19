n = int(input())
l = [n]
while True:
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    if n in l:
        break
    else:
        l.append(n)
print(len(l) + 1)
