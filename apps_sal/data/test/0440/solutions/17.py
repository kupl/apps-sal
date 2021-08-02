v = 'aeiouy'
n = input()
a = input()
i = 0
try:
    while i < len(a):
        while a[i] in v and a[i + 1] in v:
            a = a[:i + 1] + a[i + 2:]
        i += 1
except:
    pass
print(a)
