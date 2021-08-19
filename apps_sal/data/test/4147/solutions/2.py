import itertools
(n, a, b, c) = map(int, input().split())
l = [int(input()) for i in range(n)]
bumboo = ['A', 'B', 'C', 'D']
prod = list(itertools.product(bumboo, repeat=n))
temp = []
for i in prod:
    tempa = 0
    tempb = 0
    tempc = 0
    for j in range(n):
        if i[j] == 'A':
            tempa += l[j]
        elif i[j] == 'B':
            tempb += l[j]
        elif i[j] == 'C':
            tempc += l[j]
    if tempa * tempb * tempc == 0:
        pass
    else:
        temp.append(abs(tempa - a) + abs(tempb - b) + abs(tempc - c) + 10 * (n - 3 - i.count('D')))
print(min(temp))
