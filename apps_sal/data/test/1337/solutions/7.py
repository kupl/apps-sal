n = int(input())
slov = {}
mas = list(map(int, input().split()))
mas.sort()
kek = {}
i = 1
for b in range(1, n):
    if mas[b] == mas[b - 1]:
        i += 1
    else:
        kek[mas[b - 1]] = i
        i = 1
kek[mas[n - 1]] = i
m = int(input())
mas = list(map(int, input().split()))
mas2 = list(map(int, input().split()))
mi1 = -1
mi2 = -1
otv = 0
for i in range(m):
    try:
        a = kek[mas[i]]
    except:
        a = 0
    try:
        b = kek[mas2[i]]
    except:
        b = 0
    if a > mi1:
        mi1 = a
        mi2 = b
        otv = i + 1
    elif a == mi1:
        if mi2 < b:
            mi2 = b
            otv = i + 1
print(otv)
