n = int(input())
dict_1 = {}
(res1, res2) = (0, 0)
for i in input().split():
    if i not in dict_1:
        dict_1[i] = 1
    else:
        dict_1[i] += 1
dict_2 = dict_1.copy()
for i in input().split():
    dict_1[i] -= 1
for i in dict_1:
    if dict_1[i]:
        res1 = i
        break
dict_2[res1] -= 1
for i in input().split():
    dict_2[i] -= 1
for i in dict_2:
    if dict_2[i]:
        res2 = i
        break
print(res1)
print(res2)
