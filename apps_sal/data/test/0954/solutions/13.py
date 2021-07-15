a = input()
a = a.strip()
razlicni = set()
razlicni.add(a)
for _ in range(len(a)):
    a = a[-1] + a[:-1]
    razlicni.add(a)
print(len(razlicni))


