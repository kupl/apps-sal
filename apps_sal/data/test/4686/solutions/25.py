w = input()
char_map = {c: 0 for c in w}
for c in w:
    char_map[c] += 1
flag = True
for val in list(char_map.values()):
    if val % 2 != 0:
        flag = False
        break
print('Yes' if flag else 'No')
