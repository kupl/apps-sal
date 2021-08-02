n = int(input())
l = list(map(int, input().split()))
a = l[0]
dup = []
suma = a
for i in range(1, n):
    if l[i] <= a // 2:
        dup.append(i)
        suma += l[i]
if suma * 2 <= sum(l):
    print(0)
else:
    print(len(dup) + 1)
    print(1, end=" ")
    for i in dup:
        print(i + 1, end=" ")
