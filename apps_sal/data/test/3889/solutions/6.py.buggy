n = int(input())

cnt = [0] * 26

s = input()
for c in s:
    cnt[ord(c) - ord('a')] += 1

for u in cnt:
    if u > 1:
        print('Yes')
        return

if cnt.count(0) == 25:
    print('Yes')
else:
    print('No')
