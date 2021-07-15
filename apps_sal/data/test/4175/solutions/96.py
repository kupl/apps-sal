n = int(input())
list_w = [input() for s in range(0, n)]
for i in range(0, n):
    if i == 0 or (list_w[i - 1][-1] == list_w[i][0]) and list_w[i] not in list_w[:i]:
        continue
    else:
        print("No")
        return
print("Yes")
