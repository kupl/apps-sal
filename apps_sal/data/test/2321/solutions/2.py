t = int(input())
for _ in range(t):
    input()
    s = input()
    pref_len = 0
    for c in s:
        if c != '<':
            break
        pref_len += 1
    suf_len = 0
    for c in reversed(s):
        if c != '>':
            break
        suf_len += 1
    print(min(suf_len, pref_len))

