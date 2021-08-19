s = str(input())
cnt = 0
for i in range(3):
    if s[i] == 'o':
        cnt += 1
    else:
        continue
print(700 + 100 * cnt)
