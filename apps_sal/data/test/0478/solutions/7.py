def go():
    n = int(input())
    # b = list(map(int, input().split()))
    s = list(map(ord, input()))
    letters = sorted(set(s), reverse=True)
    for l in letters:
        l1 = l - 1
        if l - 1 not in letters:
            continue
        i = 0
        while i < len(s):
            if s[i] != l1:
                i += 1
            elif i > 0 and s[i - 1] == l:
                del s[i - 1]
                i -= 1
            elif i < len(s) - 1 and s[i + 1] == l:
                del s[i + 1]
            else:
                i += 1
    # print(''.join(map(chr,s)))
    return n - len(s)


print(go())
