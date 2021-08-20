n = int(input())
kuro = input()
shiro = input()
katie = input()
words = [kuro, shiro, katie]
bank = [[0 for i in range(0, ord('z') - ord('A') + 1)] for j in range(0, 3)]
for i in range(0, 3):
    for l in words[i]:
        bank[i][ord(l) - 65] += 1
    summ = sum(bank[i])
    if summ == max(bank[i]) and n == 1:
        for j in range(0, 52):
            if bank[i][j] == summ:
                bank[i][j] -= 2
                break
kuro = min(len(words[0]), max(bank[0]) + n)
shiro = min(len(words[1]), max(bank[1]) + n)
katie = min(len(words[2]), max(bank[2]) + n)
if kuro > shiro and kuro > katie:
    print('Kuro')
elif shiro > kuro and shiro > katie:
    print('Shiro')
elif katie > kuro and katie > shiro:
    print('Katie')
elif katie == shiro or katie == kuro or shiro == kuro:
    print('Draw')
