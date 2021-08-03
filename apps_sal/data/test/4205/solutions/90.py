N = int(input())
lst1 = list(map(int, input().split()))
lst2 = sorted(lst1)
c = 0
for i, j in zip(lst1, lst2):
    if i != j:
        c += 1

if c == 2 or c == 0:
    print('YES')

else:
    print('NO')
