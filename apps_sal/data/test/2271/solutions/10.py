def UpperBound(A, key):
    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] > key:
            right = middle
        else:
            left = middle
    return right


n = int(input())
masa = []
masb = []
mas = []
for i in range(n - 1):
    mas.append(input().split())
s = 0
for i in range(n - 1):
    masa.append(int(mas[i][0]))
    masb.append(int(mas[i][1]))
masa.sort()
masb.sort()
for i in range(len(masb)):
    foun = UpperBound(masa, masb[i])
    xx = masa[i:foun].count(masb[i])
    s = s + xx
for i in range(len(masa)):
    foun = UpperBound(masa, masa[i])
    xx = masa[i + 1:foun].count(masa[i])
    s = s + xx
for i in range(len(masa)):
    foun = UpperBound(masb, masa[i])
    xx = masb[i + 1:foun].count(masa[i])
    s = s + xx
for i in range(len(masb)):
    foun = UpperBound(masb, masb[i])
    xx = masb[i + 1:foun].count(masb[i])
    s = s + xx
print(s)
