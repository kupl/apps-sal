(n, k) = input().split()
k = 10 ** int(k)
a = len(n) - 1
s = 0
while int(n) % k != 0:
    for i in range(len(n) - 1, -1, -1):
        if n[i] != '0':
            n = n[:i] + n[i + 1:]
            s += 1
            break
print(a if set(list(n)) == {'0'} else s)
