s = input()
chuj = [ord(s[i]) for i in range(len(s))]
n = len(chuj)
print('Mike')
mini = 100000
for i in range(1, n):
    mini = min(mini, chuj[i - 1])
    if mini < chuj[i]:
        print('Ann')
    else:
        print('Mike')
