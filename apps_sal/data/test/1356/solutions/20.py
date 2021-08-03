s = input()

cnt = 0
for elem in s:
    if elem == 'a':
        cnt += 1
print(min(len(s), max(cnt * 2 - 1, 0)))
