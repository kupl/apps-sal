S = input()
T = input()

characters_num = len(T)

for i in range(characters_num):
    rotation_S = S[i:] + S[:i]
    if rotation_S == T:
        answer = 'Yes'
        break
    else:
        answer = 'No'
print(answer)
