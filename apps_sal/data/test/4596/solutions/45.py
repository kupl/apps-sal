n = int(input())
list_a = [int(i) for i in input().split()]
ans = 0
flag = True
while flag:
    for i in range(0, len(list_a)):
        if list_a[i] % 2 == 0:
            list_a[i] = list_a[i] // 2
        else:
            flag = False
            break

        if i == len(list_a) - 1:
            ans += 1

print(ans)
