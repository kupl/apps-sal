from collections import Counter
s = input()
if len(s) < 26:
    print(-1)
else:
    a = Counter(s[:26])
    score = len(a)
    if '?' in a:
        score += a['?'] - 1
    ans = []
    if score == 26:
        for c in s[:26]:
            if c == '?':
                for z in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if not a[z]:
                        a[z] = 1
                        ans += z
                        break
            else:
                ans += c
        for c in s[26:]:
            ans += 'A' if c == '?' else c
        print(''.join(ans))
    else:
        for (i, c) in enumerate(s[26:]):
            p = s[i]
            ans += 'A' if p == '?' else p
            a[p] -= 1
            if p == '?' or a[p] == 0:
                score -= 1
            a[c] += 1
            if c == '?' or a[c] == 1:
                score += 1
            if score == 26:
                for c in s[i + 1:i + 27]:
                    if c == '?':
                        for z in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                            if not a[z]:
                                a[z] = 1
                                ans += z
                                break
                    else:
                        ans += c
                for c in s[i + 27:]:
                    ans += 'A' if c == '?' else c
                print(''.join(ans))
                break
        else:
            print(-1)
