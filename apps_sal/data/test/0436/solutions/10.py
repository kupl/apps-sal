n = int(input())
l = list(map(int, input().split()))
a = l[0]
total = sum(l)
ans = [1]
seats = a
for i in range(1, n):
    if a >= 2 * l[i]:
        ans.append(i + 1)
        seats += l[i]
if seats > total // 2:
    print(len(ans))
    for i in ans:
        print(i, end=' ')
else:
    print(0)
