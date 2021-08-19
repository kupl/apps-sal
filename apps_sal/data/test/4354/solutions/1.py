(n, m) = map(int, input().split())
num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))
check_list = []
for i in range(m):
    check_list.append(list(map(int, input().split())))
for i in range(n):
    d = 10 ** 9
    h = 0
    for j in range(m):
        if d > abs(num_list[i][0] - check_list[j][0]) + abs(num_list[i][1] - check_list[j][1]):
            d = abs(num_list[i][0] - check_list[j][0]) + abs(num_list[i][1] - check_list[j][1])
            h = j + 1
    print(h)
