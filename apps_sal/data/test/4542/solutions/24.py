from collections import Counter
S = input()

c = Counter(S)
if c['W'] == 0 or c['B'] == 0:
    print((0))
    return

now = ''
count = 0
for i in range(len(S)):
    if i == 0:
        now = S[i]
        continue
    if now == S[i]:
        continue
    else:
        count += 1
        now = S[i]
        continue

print(count)

