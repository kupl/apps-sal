s = input()

words = [w for w in s]

cnt = 0
for r in range(len(words) - 1):
    if words[r+1] == words[r]:
        if words[r+1] == '0':
            words[r+1] = '1'
        else:
            words[r+1] = '0'
        cnt += 1

print(cnt)
