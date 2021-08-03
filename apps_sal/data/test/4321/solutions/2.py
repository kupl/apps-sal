n, k = input().split()
k = int(k)
n = n[::-1]

for i in range(k):
    if n[0] == '0':
        n = n[1:]
    else:
        n = chr(ord(n[0]) - 1) + n[1:]

print(n[::-1])
