n = int(input())
s, t = map(str, input().split())
new_word_list = []

for i in range(n):
    new_word_list.append(s[i])
    new_word_list.append(t[i])

print(''.join(new_word_list))
