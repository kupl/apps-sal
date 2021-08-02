N = int(input())

li = [input() for i in range(N)]

temp = li[0][-1]
for j in range(N - 1):
    if temp == li[j + 1][0]:
        temp = li[j + 1][-1]
    else:
        print("No")
        return
li.sort()

for k in range(N - 1):
    if li[k] == li[k + 1]:
        print("No")
        return
print("Yes")
