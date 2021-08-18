N = int(input())
a = list(map(int, input().split()))

mini = 0
color_list = []
for i in a:
    if (i // 400) < 8 and ((i // 400 in color_list) == False):
        mini += 1
        color_list.append(i // 400)

maxi = mini
for j in a:
    if j >= 3200:
        maxi += 1
if mini == 0:
    mini = 1
print(mini, maxi)
