S = input()
ok = 1
for i in range(len(S)):
    if i % 2 == 1 and S[i] == 'R':
        ok = 0
    if i % 2 == 0 and S[i] == 'L':
        ok = 0
print('Yes' if ok else 'No')
