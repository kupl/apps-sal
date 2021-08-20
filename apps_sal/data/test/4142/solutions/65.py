s = input()
n = len(s)
res = 'Yes'
for i in range(n):
    if i % 2 == 0:
        if s[i] == 'L':
            res = 'No'
    elif s[i] == 'R':
        res = 'No'
print(res)
