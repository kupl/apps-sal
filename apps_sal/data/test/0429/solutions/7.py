def fill_uniq(nice,cts):
    l_nice = list(nice)
    letters = [chr(ord('A')+i) for i in range(26) if not cts[i]]
    l_i = 0
    for i,c in enumerate(l_nice):
        if c == '?':
            l_nice[i] = letters[l_i]
            l_i += 1
    return ''.join(l_nice)

def ans(s, i, cts):
    nice = s[i:i+26]
    return s[:i].replace('?','A') + fill_uniq(nice,cts) + s[i+26:].replace('?','A')

def main():
    s = input()

    if len(s) < 26:
        print(-1)
        return

    cts = [0]*26
    for c in s[:26]:
        if c == '?': continue
        cts[ord(c)-ord('A')] += 1
    max_ct = max(cts)
    if max_ct <= 1:
        print(ans(s,0,cts))
        return

    for i in range(1,len(s) - 26+1):
        if s[i-1] != '?':
            cts[ord(s[i-1]) - ord('A')] -= 1
        if s[i+25] != '?':
            cts[ord(s[i+25]) - ord('A')] += 1
        #print(s[i-1], i,cts,sum(cts))
        max_ct = max(cts)
        if max_ct <= 1:
            print(ans(s,i,cts))
            return
    print(-1)

main()

