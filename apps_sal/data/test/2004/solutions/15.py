n = int(input())

ans = []
for i in range(n):
    if i % 2 == 1:
        ans.append(i)
for i in range(n):
    if i % 2 == 0:
        ans.append(i)
for i in range(n):
    if i % 2 == 1:
        ans.append(i)
print(len(ans))
print(' '.join([str(i + 1) for i in ans]))
