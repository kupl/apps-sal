n = int(input())
t = ' '.join((input() for i in range(n)))
ans = 0
for i in 'abcdefghijklmnopqrstuvwxyz':
    if not i in t:
        ans = i
        break
if not ans:
    for i in 'abcdefghijklmnopqrstuvwxyz':
        for j in 'abcdefghijklmnopqrstuvwxyz':
            if not i + j in t:
                ans = i + j
                break
        if ans:
            break
print(ans)
