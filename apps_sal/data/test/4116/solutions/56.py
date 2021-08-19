n = int(input())
ans = list()
for i in range(1, 10):
    for j in range(1, 10):
        ans.append(i * j)
if n in ans:
    print('Yes')
else:
    print('No')
