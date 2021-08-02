
# int(input())
# [int(i) for i in input().split()]

n = int(input())
a = [int(i) for i in input().split()]
ind = [int(i) for i in input()]
ind.append(0)

b = []
curr = 0

for i in range(n):
    if not ind[i]:

        tmp = a[curr:i + 1]
        tmp.sort()
        b.extend(tmp)
        curr = i + 1

# print(b)
if all(b[i] <= b[i + 1] for i in range(n - 1)): print("YES")
else: print('NO')
