N = int(input())
i = 0
j = 0
num = []
new = []
k = 0
total = 0
isSorted = False
flagDouble = False
IN = input().split()
while i < N:
    k = int(IN[i])
    num.append((k, i))
    new.append(k)
    if i == new[i]:
        total = total + 1
    i = i + 1
if total == N:
    isSorted = True
else:
    num.sort()
for i in range(N):
    j = num[i][1]
    if i == new[j] and j == new[i] and (i != j):
        flagDouble = True
if flagDouble:
    print(total + 2)
elif not isSorted:
    print(total + 1)
else:
    print(total)
