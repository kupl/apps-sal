n = int(input())
F = [1, 2]
for i in range(100):
    F.append(F[-1] + F[-2])
F = set(F)
s = ''.join(('O' if i in F else 'o' for i in range(1, n + 1)))
print(s)
