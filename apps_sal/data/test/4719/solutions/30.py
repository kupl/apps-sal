n = int(input())

a = [99] * 26
for i in range(n):
    s = input()
    tmp = [0] * 26
    for c in s:
        x = ord(c) - ord('a')
        tmp[x] += 1
    for j in range(26):
        a[j] = min(a[j], tmp[j])

for i in range(26):
    c = chr(i + ord('a'))
    print(c * a[i], end='')
print()

