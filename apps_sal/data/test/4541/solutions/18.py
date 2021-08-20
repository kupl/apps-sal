c = input()
lists = ['a', 'e', 'i', 'u', 'o']
answer = 'consonant'
for i in lists:
    if c == i:
        answer = 'vowel'
print(answer)
