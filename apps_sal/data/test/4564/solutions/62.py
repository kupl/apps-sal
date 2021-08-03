s = input()
letters = []
ans = 'yes'
for i in s:
    if i in letters:
        ans = 'no'
        break
    else:
        letters.append(i)
print(ans)
