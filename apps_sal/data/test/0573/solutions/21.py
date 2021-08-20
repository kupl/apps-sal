n = int(input())
tab = [0, 0]
for a in input().split():
    if a == '1':
        tab[0] += 1
    else:
        tab[1] += 1
nums_of_cb = min([tab[0], tab[1]])
print(nums_of_cb + (tab[0] - nums_of_cb) // 3)
