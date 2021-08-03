a, b = list(map(int, input().split()))
s = input()

ans = True

for (i, char) in enumerate(s):
    if i == a:
        if char == '-':
            ans = True
        else:
            ans = False
            break
    else:
        try:
            ans = type(int(char)) is int
        except:
            ans = False
            break

if ans:
    print('Yes')
else:
    print('No')
