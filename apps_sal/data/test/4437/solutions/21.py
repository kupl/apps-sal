input()
smth = list(input())
cnt = 0
for i in range(len(smth) // 2):
    if smth[i * 2] == smth[i * 2 + 1]:
        cnt += 1
        if smth[i * 2] == 'a':
            smth[i * 2] = 'b'
        else:
            smth[i * 2] = 'a'
smth = ''.join(smth)
print(cnt)
print(smth)
