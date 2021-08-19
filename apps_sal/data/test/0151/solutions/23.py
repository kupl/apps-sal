word = input()
l = ['a', 'e', 'i', 'o', 'u']
curr_s = []
i = 0
for j in range(len(word)):
    if word[j] not in l:
        if curr_s.count(word[j]) > 1:
            continue
        curr_s.append(word[j])
        if len(curr_s) > 2:
            print(word[i:j], end=' ')
            curr_s = [word[j]]
            i = j
    else:
        curr_s = []
print(word[i:])
