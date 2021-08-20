s = input()
a = [ord(c) - ord('a') + 1 for c in s]
res = [0] * len(s)
mi = a[0]
print('Mike')
for i in range(1, len(s)):
    if a[i] > mi:
        print('Ann')
    else:
        mi = a[i]
        print('Mike')
