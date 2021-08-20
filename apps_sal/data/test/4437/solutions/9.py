n = int(input())
a = list(map(lambda x: 0 if x == 'a' else 1, input()))
bal = 0
for i in range(1, n, 2):
    if a[i] == a[i - 1]:
        bal += 1
        a[i] = (a[i - 1] + 1) % 2
print(bal)
print(''.join(('a' if a[i] == 0 else 'b' for i in range(n))))
