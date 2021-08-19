len_str = int(input())
a_str = list(input())
b_str = list(input())
ans = 0
idx_range = int(len_str / 2) if len_str % 2 == 0 else int(len_str / 2) + 1
for idx in range(idx_range):
    a_char = [a_str[idx], a_str[len_str - idx - 1]]
    b_char = [b_str[idx], b_str[len_str - idx - 1]]
    char_dict = dict()
    for a in a_char:
        if a in char_dict:
            char_dict[a] += 1
        else:
            char_dict[a] = 1
    for b in b_char:
        if b in char_dict:
            char_dict[b] += 1
        else:
            char_dict[b] = 1
    if len(char_dict) == 1 or (len(char_dict) == 2 and char_dict[a_char[0]] == 2):
        continue
    elif b_char[0] == b_char[1]:
        ans += 1
    elif char_dict[b_char[0]] == 2 or char_dict[b_char[1]] == 2:
        ans += 1
    elif char_dict[b_char[0]] == 3 or char_dict[b_char[1]] == 3:
        ans += 1
    else:
        ans += 2
if len_str % 2 == 1:
    mid_idx = int(len_str / 2)
    if a_str[mid_idx] != b_str[mid_idx]:
        ans += 1
print(ans)
