n = 3
num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))

N = int(input())

list1 = [int(input()) for _ in range(N)]

list2 = []
i = 0
while i <= 2:
    j = 0
    while j <= 2:
        list2.append(num_list[i][j])
        j = j + 1
    i = i + 1

s = 0
for k in list2:
    if list1.count(k) == 1:
        list2[s] = 101
        s = s + 1
    else:
        s = s + 1
        continue

if list2[0] + list2[1] + list2[2] == 303:
    print('Yes')
elif list2[3] + list2[4] + list2[5] == 303:
    print('Yes')
elif list2[6] + list2[7] + list2[8] == 303:
    print('Yes')
elif list2[0] + list2[3] + list2[6] == 303:
    print('Yes')
elif list2[1] + list2[4] + list2[7] == 303:
    print('Yes')
elif list2[2] + list2[5] + list2[8] == 303:
    print('Yes')
elif list2[0] + list2[4] + list2[8] == 303:
    print('Yes')
elif list2[2] + list2[4] + list2[6] == 303:
    print('Yes')
else:
    print('No')
