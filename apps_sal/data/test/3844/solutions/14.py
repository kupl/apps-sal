n = int(input())
a = [int(i) for i in input().split()]
a.sort()
counts = []
curr = 1
for i in range(1, n):
    if a[i - 1] != a[i]:
        counts.append(curr)
        curr = 1
    else:
        curr += 1
counts.append(curr)
m = len(counts)
ans = False
for i in range(m):
    if counts[i] % 2 == 1:
        ans = True
        continue
if ans:
    print('Conan')
else:
    print('Agasa')
