def werify_message(words, message):
    true_message = ''.join(['<3', '<3'.join(words), '<3'])
    i = 0
    for litera in message:
        if len(true_message) != i:
            if litera == true_message[i]:
                i += 1
        else:
            return 'yes'
    if i == len(true_message):
        return 'yes'
    else:
        return 'no'


n = int(input())
words = list()
for i in range(n):
    word = input()
    words.append(word)
message = input()
print(werify_message(words, message))
