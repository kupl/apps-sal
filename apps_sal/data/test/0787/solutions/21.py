k = int(input())
string = input()
first_char_set = set()
length = len(string)
unique_mnt = 0
res_ind = []
if k > length:
    print("NO")
    return
if k == 1:
    print("YES")
    print(string)
    return
for i in range(length):
    c = string[i]
    if not(c in first_char_set):
        unique_mnt += 1
        first_char_set.add(c)
        res_ind.append(i)
if k > len(res_ind):
    print("NO")
    return
res = []
res_len = len(res_ind)
for i in range(res_len - 1):
    cur_ind = res_ind[i]
    next_ind = res_ind[i + 1]
    if k > 1:
        res.append(string[cur_ind:next_ind])
        k -= 1
    elif k == 1:
        res.append(string[cur_ind:])
        k -= 1
        break
if k == 1:
    res.append(string[next_ind:])
print("YES")
for el in res:
    print(el)
