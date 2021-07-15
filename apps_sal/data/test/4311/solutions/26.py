s = int(input())
list_a = [None]
list_a.append(s)
ans = 0
for i in range(1, 10 ** 6 + 1):
    if list_a[i] % 2 == 0:
        list_a.append(list_a[i] // 2)
    else:
        list_a.append(3 * list_a[i] + 1)
    if list_a[i] in list_a[:i]:
        ans = i
        break
print(ans)
