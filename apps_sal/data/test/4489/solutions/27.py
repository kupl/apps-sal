words = {'': 0}
N = int(input())
for i in range(N):
    word = input()
    words[word] = words.get(word, 0) + 1
M = int(input())
for i in range(M):
    word = input()
    words[word] = words.get(word, 0) - 1
print(max(words.values()))
