L = ['A', 'C', 'G', 'T']

s = input()
cnt = [0] * len(s)

for i in range(len(s)):
    for j in range(i, len(s)):
        if s[j] in L:
            cnt[i] += 1
        else:
            break
print((max(cnt)))
