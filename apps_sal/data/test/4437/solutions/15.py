n = int(input())
a = list(input())
# ans = a.copy()
l = 0
for i in range(1, n, 2):
    if a[i] == a[i - 1]:
        l += 1
        a[i] = 'a' if a[i - 1] == 'b' else 'b'

print(l)
print(''.join(a))
