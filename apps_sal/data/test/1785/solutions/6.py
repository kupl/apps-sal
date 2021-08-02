n = int(input())
s = input()
lst = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
k, l = 0, 1
for i in s:
    lst[i] += 1
    if k < lst[i]:
        k = lst[i]
        l = 1
    else:
        if k == lst[i]:
            l += 1
print(l ** n % (10 ** 9 + 7))
