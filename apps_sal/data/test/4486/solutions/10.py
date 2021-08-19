S = list(input())
new_list = ''
for i in range(len(S)):
    if i % 2 == 0:
        new_list += S[i]
print(new_list)
