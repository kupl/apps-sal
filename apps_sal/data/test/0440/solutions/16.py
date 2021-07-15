n = int(input())
s = list(input())
gl = ['a', 'e', 'i', 'o', 'u', 'y']
x = -1
uber = []
k = 0
for i in range(n - 1):
    if s[i] in gl and s[i + 1] in gl:
        uber.append(i + 1)
for i in uber:
    s.pop(i - k)
    k += 1
print(''.join(s))
