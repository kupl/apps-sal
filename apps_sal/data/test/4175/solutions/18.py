N = int(input())
li = []
flag = True
for i in range(N):
    word = input()
    if i != 0:
        if pre_word[len(pre_word)-1] != word[0] or word in li:
            flag = False
            break
    li.append(word)
    pre_word = word
if flag:
    print('Yes')
else:
    print('No')
