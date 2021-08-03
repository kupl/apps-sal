a, b = map(int, input().split())
s = input()
x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
if s[a] != '-':
    print('No')
    return
s = list(s)
del s[a]
for i in s:
    if i not in x:
        print('No')
        return
print('Yes')
