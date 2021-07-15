n = int(input())
a = [int(i) for i in input().split()][::-1]
al = 0
i = 0
mk = 0
while i < n:
    if mk == 0:
        al += 1
    mk = max(0, mk - 1)
    mk = max(mk, a[i])
    i += 1
print(al)
