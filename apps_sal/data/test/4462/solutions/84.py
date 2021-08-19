input()
a = list(map(int, input().split()))
(b1, b2, b4) = ([], [], [])
ans = ''
for i in a:
    if i % 2 != 0:
        b1.append(i)
    elif i % 4 == 0:
        b4.append(i)
    elif i % 2 == 0:
        b2.append(i)
if b2:
    if len(b1) <= len(b4):
        ans = 'Yes'
    else:
        ans = 'No'
elif len(b1) <= len(b4) + 1:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
