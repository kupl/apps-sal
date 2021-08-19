S = input()
T = input()
num = len(T)
for i in range(num):
    rotation_S = S[i:] + S[:i]
    if rotation_S == T:
        answer = 'Yes'
        break
    else:
        answer = 'No'
print(answer)
