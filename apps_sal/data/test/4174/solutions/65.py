n, x = (int(i) for i in input().split())
list_l = [int(j) for j in input().split()]
tmp = 0
count = 0
for i in range(0, n + 1):
    if i == 0:
        pass
    else:
        tmp += list_l[i - 1]
        if tmp > x:
            break
    count += 1
print(count)
