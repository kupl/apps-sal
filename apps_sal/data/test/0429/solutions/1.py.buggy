from collections import Counter


s = input()
for i in range(len(s) - 25):
    t = s[i:i + 26]
    cnt = Counter(t)
    if len(cnt) - ('?' in cnt) + cnt['?'] == 26:
        print(s[:i].replace('?', 'A'), end='')
        cur = 'A'
        for c in t:
            if c != '?':
                print(c, end='')
            else:
                while cur in cnt:
                    cur = chr(ord(cur) + 1)
                cnt[cur] += 1
                print(cur, end='')
        print(s[i + 26:].replace('?', 'A'))
        return
print(-1)
