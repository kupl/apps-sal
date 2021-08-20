t = int(input())
for j in range(t):
    n = list(input())
    r = 0
    ans = []
    for i in range(len(n) - 2):
        if len(n) - 4 > i and n[i] == 't' and (n[i + 1] == 'w') and (n[i + 2] == 'o') and (n[i + 3] == 'n') and (n[i + 4] == 'e'):
            r += 1
            ans.append(i + 3)
            n[i + 2] = '#'
        elif n[i] == 'o' and n[i + 1] == 'n' and (n[i + 2] == 'e') or (n[i] == 't' and n[i + 1] == 'w' and (n[i + 2] == 'o')):
            r += 1
            ans.append(i + 2)
            n[i + 1] = '#'
    print(r)
    print(*ans)
