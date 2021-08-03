n = int(input())
sem1 = []
sem2 = []
l = [0, 0]
for cont in range(0, n):
    l = list(map(int, input().split()))
    sem1.append(l[0])
    sem2.append(l[1])

kmax = int(n / 2)
max1 = 0
max2 = 0

for cont in range(0, n):
    if sem1[max1] < sem2[max2]:
        max1 += 1
    else:
        max2 += 1

ris1 = ['1'] * (max([max1, kmax]))
ris2 = ['1'] * max([max2, kmax])
ris1 = ris1 + ['0'] * (n - len(ris1))
ris2 = ris2 + ['0'] * (n - len(ris2))

print(''.join(ris1))
print(''.join(ris2))
