n = int(input())
x_list = []
y_list = []
h_list = []

for i in range(n):
    a, b, c = list(map(int, input().split()))
    x_list.append(a)
    y_list.append(b)
    h_list.append(c)

k = h_list.index(max(h_list))

for x in range(101):
    for y in range(101):
        h_max = h_list[k] + abs(x_list[k] - x) + abs(y_list[k] - y)

        for j in range(n):
            if h_list[j] == 0:
                if h_max - (abs(x_list[j] - x) + abs(y_list[j] - y)) > 0:
                    h_max = -1
            else:
                if h_max != abs(x_list[j] - x) + abs(y_list[j] - y) + h_list[j]:
                    h_max = -1

        if h_max != -1:
            print((str(x) + ' ' + str(y) + ' ' + str(h_max)))
            break
