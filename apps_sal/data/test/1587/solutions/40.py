N = int(input())
S = input()
Answer = 0
White = 0
Red = S.count('R')
for j in range(len(S)):
    i = S[j]
    if i == 'W':
        White += 1
    elif i == 'R' and White > 0 and j + 1 > Red:
        Answer += 1
        White -= 1
print(Answer)
