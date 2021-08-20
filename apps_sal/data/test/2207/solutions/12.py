x = input().split()
r = int(x[0])
mas = ''
for i in range(r):
    if i + 1 == r:
        mas = input()
        mas = mas + '.'
        mas = '.' + mas
    else:
        input()
g = 0
for i in range(len(mas) - 1):
    if mas[i] != mas[i + 1]:
        g = g + 1
print(int(g / 2))
