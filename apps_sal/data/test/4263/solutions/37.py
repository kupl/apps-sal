remove = ['A', 'C', 'G', 'T']
s = input()
cnt = [0] * 10
j = 0
for i in range(len(s)):
    if s[i] in remove:
        cnt[j] += 1
    else:
        j += 1

print(max(cnt))
