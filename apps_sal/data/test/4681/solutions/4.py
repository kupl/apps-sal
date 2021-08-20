N = int(input())
l1 = 2
l2 = 1
for i in range(N - 1):
    (l1, l2) = (l2, l1 + l2)
print(l2)
