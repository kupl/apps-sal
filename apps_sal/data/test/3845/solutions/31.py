a, b = map(int, input().split())
line = ''.join(['.#'] * 50)
dot = ['.', '#']
cl = [''.join(['.'] * 100), ''.join(['#'] * 100)]
ba = [b - 1, a - 1]
ans = []
y = ans.append
for c in [0, 1]:
    y(cl[c])
    for i in range(ba[c] // 50):
        y(line)
        y(cl[c])
    y(''.join(['.#'] * (ba[c] % 50)) + cl[c][(ba[c] % 50) * 2:])
    y(cl[c])
print(len(ans), 100)
for l in ans:
    print(''.join(l))
