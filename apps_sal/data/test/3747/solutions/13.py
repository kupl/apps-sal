n = input()
cnt = [0] * 7
for i in range(len(n)):
    if n[i] == 'B':
        cnt[0] += 1
    elif n[i] == 'u':
        cnt[1] += 1
    elif n[i] == 'l':
        cnt[2] += 1
    elif n[i] == 'b':
        cnt[3] += 1
    elif n[i] == 'a':
        cnt[4] += 1
    elif n[i] == 's':
        cnt[5] += 1
    elif n[i] == 'r':
        cnt[6] += 1
cnt[4] //= 2
cnt[1] //= 2
print(min(cnt))
