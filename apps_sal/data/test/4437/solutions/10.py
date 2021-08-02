n = int(input())
s = str(input())
k = 0
new = ''

for i in range(0, n - 1, 2):
    if s[i:i + 2] == 'ab':
        new += 'ab'
        continue
    if s[i:i + 2] == 'ba':
        new += 'ba'
        continue
    else:
        k += 1
        new += 'ab'

print(k)
print(new)
