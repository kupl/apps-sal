N = int(input())
word_list = []
for i in range(N):
    word_list.append(input())
print(len(set(word_list)))
