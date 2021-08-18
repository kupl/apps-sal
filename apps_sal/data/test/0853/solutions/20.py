
import string

n = int(input())

str = input()
L = str.split()
S = 0
Szero = 0
Sfive = 0

while n > 0:
    S += int(L[n - 1])
    if int(L[n - 1]) == 0:
        Szero += 1
    else:
        Sfive += 1
    n -= 1

newstr = ""

if Sfive >= 9 and Szero > 0:

    i = int(Sfive / 9)
    i = i * 9
    while i > 0:
        newstr += '5'
        i -= 1

    i = Szero

    while i > 0:
        newstr += '0'

        i -= 1

    print(newstr)
elif Sfive < 9 and Szero > 0:
    print("0")
else:
    print("-1")
