import string
w = list(map(str, input()))
ans = ''
alp = list(map(str, string.ascii_lowercase))
for char in alp:
    if w.count(char) % 2 == 0:
        ans = 'Yes'
    else:
        ans = 'No'
        break
print(ans)
