x = input()
boys = list(map(int, input().split(' ')))
y = input()
girls = list(map(int, input().split(' ')))
boys.sort()
girls.sort()
ok = 0
for i in boys[:]:
    if i - 1 in girls:
        girls.remove(i - 1)
        boys.remove(i)
        ok += 1
    elif i in girls:
        girls.remove(i)
        boys.remove(i)
        ok += 1
    elif i + 1 in girls:
        girls.remove(i + 1)
        boys.remove(i)
        ok += 1
print(ok)
