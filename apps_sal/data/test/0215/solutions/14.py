input()
s = input()
arr = []
temp = ''
for x in s:
    if ord(x) <= ord('Z'):
        if temp != '':
            arr.append(temp)
            temp = ''
    else:
        temp += x
if temp != '':
    arr.append(temp)
ans = 0
for y in arr:
    ans = max(ans, len(set(list(y))))
print(ans)
