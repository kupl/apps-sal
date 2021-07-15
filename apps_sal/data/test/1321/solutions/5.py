n = int(input())
wh = []
all_w = 0
max_h = 0
not_sorted = []
for i in range(n):
    current = list(map(int, input().split()))
    max_h = max(max_h, current[1])
    all_w += current[0]
    wh.append(current[::-1])
    not_sorted.append(current)
wh.sort()
for i in range(n):
    if not_sorted[i][1] == max_h:
        print((all_w-not_sorted[i][0])*wh[-2][0], end=" ")
    else:
        print((all_w-not_sorted[i][0])*max_h, end=" ")

