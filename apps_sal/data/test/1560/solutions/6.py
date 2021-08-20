n = int(input())
w = input().strip()
red_1 = 0
red_2 = 0
bck_1 = 0
bck_2 = 0
for i in range(len(w)):
    if w[i] == 'r':
        if i % 2:
            red_2 += 1
        else:
            red_1 += 1
    if w[i] == 'b':
        if i % 2:
            bck_2 += 1
        else:
            bck_1 += 1
print(min(max(red_2, bck_1), max(bck_2, red_1)))
