dict = {}
ans = {}
for i in range(-1, 100110):
    dict[i] = []
    ans[i] = 0
for i in range(2, 100010):
    if dict[i] == []:
        j = i + i
        while j <= 100010:
            tmp = dict[j]
            tmp += [i]
            dict[j] = tmp
            j += i
        dict[i] = [i]
n = input()
n = input()
n = n.split(" ")
banyak = 0
for i in n:
    tmp = int(i)
    for j in dict[tmp]:
        ans[j] += 1
        if ans[j] > banyak:
            banyak = ans[j]
if (banyak == 0):
    banyak = 1
print(banyak)
