k = int(input())
candili = []
for i in range(1, 1000):
    candili.append(i)

tmpli = []
for i in candili:
    for j in range(1, 15):
        tmpli.append(int(str(i) + "9" * j))
tmpli = list(set(tmpli))

tmp2li = []
for i in tmpli:
    if i <= 10 ** 15:
        tmp2li.append(i)
candili += tmp2li
candili = list(set(candili))
candili.sort()


def S(n):
    return sum(int(i) for i in str(n))


conli = []

for i in candili:
    conli.append(i / S(i))

ansli = []
for i in range(len(conli)):
    for j in range(i, len(conli)):
        if conli[i] > conli[j]:
            break
    else:
        ansli.append(candili[i])

for i in range(k):
    print(ansli[i])
