n = int(input())
list1 = list(map(int, input().split()))
replacee = [-1] * n
cnt = 0
swap = False
for i in range(n):
    if list1[i] == i:
        cnt += 1
    else:
        replacee[i] = list1[i]
for i in range(n):
    if replacee[replacee[i]] == i and (not swap):
        swap = True
        cnt += 2
if swap:
    print(cnt)
elif replacee != [-1] * n:
    print(cnt + 1)
else:
    print(cnt)
