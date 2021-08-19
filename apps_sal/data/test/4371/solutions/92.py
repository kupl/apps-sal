s = input()
a = []
for i in range(len(s) - 2):
    a.append(int(s[i] + s[i + 1] + s[i + 2]))
for i in range(len(a)):
    a[i] = abs(a[i] - 753)
print(min(a))
