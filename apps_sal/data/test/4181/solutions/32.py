N = int(input())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
c = sum(list_a)
for i in range(1, len(list_a)):
    temp = list_a[i] - min(list_a[i - 1] - list_b[i - 1], 0) * -1
    if list_a[i - 1] - list_b[i - 1] <= 0:
        list_a[i - 1] = 0
    else:
        list_a[i - 1] -= list_b[i - 1]
    if temp != list_a[i] and temp >= 0:
        list_a[i] = temp
    elif temp <= 0:
        list_a[i] = 0
del_c = sum(list_a)
ans = c - del_c
print(ans)
