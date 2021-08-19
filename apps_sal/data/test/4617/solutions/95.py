(word1, word2) = [input() for i in range(2)]
if word1[0] == word2[2] and word1[1] == word2[1] and (word1[2] == word2[0]):
    print('YES')
else:
    print('NO')
