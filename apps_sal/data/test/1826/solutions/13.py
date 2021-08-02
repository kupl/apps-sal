n = int(input())
s = input()
i = 0
cnt = 0
while i < (n - 1):
    if s[i:i + 2] == 'UR' or s[i:i + 2] == 'RU':
        cnt += 1
        i += 2
    else:
        i += 1

print(n - cnt)
