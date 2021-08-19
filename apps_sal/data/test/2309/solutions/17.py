n = int(input())

vowels = {'a', 'e', 'o', 'i', 'u'}

words = []
for i in range(n):
    words.append(input())


all_pairs = {}
sec_pairs = {}

for item in words:
    cnt, last = 0, -1
    for i in item:
        if i in vowels:
            cnt += 1
            last = i

    # all_pairs
    if cnt not in all_pairs:
        all_pairs[cnt] = {item: 1}
    else:
        if item in all_pairs[cnt]:
            all_pairs[cnt][item] += 1
        else:
            all_pairs[cnt][item] = 1

    # sec_pairs
    if cnt not in sec_pairs:
        sec_pairs[cnt] = {last: {item: 1}}
    else:
        if last not in sec_pairs[cnt]:
            sec_pairs[cnt][last] = {item: 1}
        else:
            if item not in sec_pairs[cnt][last]:
                sec_pairs[cnt][last][item] = 1
            else:
                sec_pairs[cnt][last][item] += 1

s_p = 0
s_list = []
for cnt in list(sec_pairs.keys()):
    for last in list(sec_pairs[cnt].keys()):
        s = 0
        cnt_l_list = []
        for word in list(sec_pairs[cnt][last].keys()):
            s += sec_pairs[cnt][last][word]
            cnt_l_list += sec_pairs[cnt][last][word] * [word]
        s_p += s // 2
        s_list.extend(cnt_l_list[:2 * (s // 2)])


all_p = 0
for cnt in list(all_pairs.keys()):
    s = 0
    for word in list(all_pairs[cnt].keys()):
        s += all_pairs[cnt][word]
    all_p += s // 2

ans = min(s_p, all_p // 2)
s_list = s_list[:2 * ans]

# undate all_p
for item in s_list:
    cnt = 0
    for i in item:
        if i in vowels:
            cnt += 1
    all_pairs[cnt][item] -= 1

f_list = []
for cnt in list(all_pairs.keys()):
    cnt_l = []
    s = 0
    for word in list(all_pairs[cnt].keys()):
        cnt_l += all_pairs[cnt][word] * [word]
        s += all_pairs[cnt][word]
    f_list.extend(cnt_l[:2 * (s // 2)])
f_list = f_list[:2 * ans]
# print(f_list)
print(ans)
# print(s_list)

for i in range(ans):
    print(f_list[2 * i], s_list[2 * i])
    print(f_list[2 * i + 1], s_list[2 * i + 1])
