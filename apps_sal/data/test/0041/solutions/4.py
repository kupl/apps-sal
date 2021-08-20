n = int(input())
l = list(map(int, input().split()))
zeroes = []
for i in range(len(l)):
    if l[i] == 0:
        zeroes.append(i)
zero = -1
for i in range(n):
    zeroes.append(zeroes[-1])
s = ''
for i in range(len(l)):
    if i > zeroes[zero + 1]:
        zero += 1
    if l[i] == 0:
        s += ' 0'
    else:
        try:
            s += ' ' + str(min(abs(i - zeroes[zero]), abs(i - zeroes[zero + 1]), abs(i - zeroes[zero + 2])))
        except:
            s += ' ' + str(min(abs(zeroes[zero + 1] - i), abs(i - zeroes[zero])))
print(s[1:])
