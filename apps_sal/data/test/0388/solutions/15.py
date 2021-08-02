# This code is dedicated to Olya S.
from random import*

n, k = list(map(int, input().split()))
s = input().split()

soliders = ['' for i in range(n)]


def newname():
    name = chr(randint(65, 90))
    for i in range(9):
        name += chr(randint(97, 122))
    return name


if s[0] == 'NO':
    soliders[0] = newname()
    soliders[1] = soliders[0]
    for j in range(2, 2 + k):
        if j > n - 1:
            break
        soliders[j] = newname()
else:
    for j in range(0, k):

        soliders[j] = newname()

for i in range(1, n - k + 1):
    if s[i] == 'YES':
        soliders[i + k - 1] = newname()
    else:
        soliders[i + k - 1] = soliders[i]


print(*soliders)
