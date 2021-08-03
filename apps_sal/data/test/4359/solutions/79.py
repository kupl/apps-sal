list_dish = [input() for i in range(0, 5)]
list_disit1 = [int(list_dish[i][-1]) for i in range(0, 5)]
marking = 0
min = 9
ans = 0
for i in range(0, 5):
    if list_disit1[i] != 0 and list_disit1[i] <= min:
        marking = i
        min = list_disit1[i]
for i in range(0, 5):
    if i == marking:
        ans += int(list_dish[i])
    else:
        ans += -(-int(list_dish[i]) // 10) * 10
print(ans)
