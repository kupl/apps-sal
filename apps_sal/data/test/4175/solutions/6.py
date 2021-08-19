n = int(input())
W = [input() for i in range(n)]
word = W[0]
words = [word]
for i in range(1, n):
    if W[i] in words or word[-1] != W[i][0]:
        print('No')
        break
    word = W[i]
    words.append(word)
else:
    print('Yes')
