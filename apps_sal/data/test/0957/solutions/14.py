inp = input()
result = 0
ans = 1
for alp in 'heidi':
    inp = inp[result:]
    result = inp.find(alp)
    if result == -1:
        ans = 0
        break

if ans:
    print('YES')
else:
    print('NO')
