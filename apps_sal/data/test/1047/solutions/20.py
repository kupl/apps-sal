n = input()
ans = int(max(list(n)))
print(ans)
for i in range(ans):
    num = ''
    for pos in range(len(n)):
        if int(n[pos]) >= i + 1:
            num += '1'
        else:
            num += '0'
    print(int(num), end=' ')
