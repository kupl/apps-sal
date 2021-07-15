n = int(input())
n2 = n
i = 1
while True:
    if (n2 > 26**i):
        n2 = n2 - 26**i
        i = i + 1
    else:
        break

lst = []

for j in range(i - 1):
    k = j + 1
    n = n - 26**k
n = n - 1
for j in range(i):
    k = i - j - 1
    x = n//(26**k)
    lst.append(x)
    n = n - 26**k*x
for j in range(len(lst)):
    if (j != len(lst) - 1):
        print(chr(int(97 + lst[j])), end = '')
    else:
        print(chr(int(97 + lst[j])))

