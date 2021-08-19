def palindrome(n):
    for i in range(0, len(n)):
        if n[i] != n[-(i + 1)]:
            return 0
    return 1


lessgo = ['a', 'h', 'i', 'm', 'o', 't', 'u', 'v', 'w', 'x', 'y']
i = list(input())
for j in range(len(i)):
    i[j] = i[j].lower()
mir = 1
for j in range(len(i)):
    if i[j] not in lessgo:
        mir = 0
if palindrome(i) == 1 and mir == 1:
    print('YES')
else:
    print('NO')
