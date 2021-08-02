n = int(input())
l1 = 2
l2 = 1
l = 1
for i in range(n - 1):
    l = l1 + l2
    l1, l2 = l2, l
print(l)
