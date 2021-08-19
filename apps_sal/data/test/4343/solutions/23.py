input()
a = input()
b = input()
x = []
y = []
for c in a:
    x.append(ord(c) - 97)
for c in b:
    y.append(ord(c) - 97)
result = [u + v for (u, v) in zip(x, y)]
for i in range(len(result) - 1, 0, -1):
    result[i - 1] += result[i] // 26
    result[i] %= 26
for (i, r) in enumerate(result):
    if r % 2 == 1:
        result[i + 1] += 26
    result[i] //= 2
r = ''.join((chr(c + 97) for c in result))
print(r)
