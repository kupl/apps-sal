n = input().strip()
for k in n[::-1]:
    ans = ''
    l = int(k)
    if l >= 5:
        l -= 5
        ans += '-O|'
    else:
        ans += 'O-|'
    for i in range(l):
        ans += 'O'
    ans += '-'
    for i in range(8 - len(ans)):
        ans += 'O'
    print(ans)
