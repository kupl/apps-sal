__author__ = 'Данила'
n = (input())
a = []
s = int(n)
min = 0
for i in range(len(n)):
    if int(n[i]) > min:
        min = int(n[i])
print(min)
while s != 0:
    s1 = str(s)
    k = ''
    for i in range(len(s1)):
        if s1[i] != '0':
            k += '1'
        else:
            k += '0'
    print(k, end = ' ')
    s -= int(k)


