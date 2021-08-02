word = input()

list_word = list(word)

if list_word.count(list_word[0]) == 2 and list_word.count(list_word[1]) == 2 and list_word.count(list_word[2]) == 2:
    print('Yes')
else:
    print('No')
