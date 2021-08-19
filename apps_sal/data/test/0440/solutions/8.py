n = int(input())
check = ['a', 'e', 'i', 'o', 'u', 'y']
a = input()
i = 1
while i < len(a):
    if a[i] in check and a[i - 1] in check:
        a = a[:i] + a[i + 1:]
    else:
        i += 1
print(a)
