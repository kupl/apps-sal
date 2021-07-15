lst = list()
lst.append(2)
lst.append(1)

n = int(input())
for i in range(2, n + 1):
    ans = lst[i - 2] + lst[i - 1]
    lst.append(ans)

print(lst[n])
