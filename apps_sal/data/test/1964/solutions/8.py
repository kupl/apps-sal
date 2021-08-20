n = int(input())
size = [int(i) for i in input().split()]
m = []
for i in range(0, n):
    m.append([])
    m[i] = [int(j) for j in input().split()]
ans = [i * 15 for i in size]
for i in range(0, n):
    sum = 0
    for j in m[i]:
        sum = sum + j * 5
    ans[i] = ans[i] + sum
min = ans[0]
for i in ans:
    if i < min:
        min = i
print(min)
