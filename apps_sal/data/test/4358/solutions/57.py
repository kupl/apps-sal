n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
li.sort()
li[-1] = li[-1] // 2
print(sum(li))
