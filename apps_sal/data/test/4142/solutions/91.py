S = str(input())
ans = 'Yes'
for i in range(1, len(S) + 1):
    not_char = ''
    if i % 2 == 0:
        not_char = 'R'
    else:
        not_char = 'L'
    if S[i - 1:i] == not_char:
        ans = 'No'
        break
print(ans)
