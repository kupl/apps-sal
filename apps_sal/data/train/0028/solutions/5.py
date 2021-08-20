def count(string, substring):
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count


for _ in range(int(input())):
    n = int(input())
    os = input()
    good = False
    for i in range(n):
        if (os[i] == 'a' or os[i] == '?') and i <= n - 7:
            s = list(os)
            bad = False
            for j in range(i, i + 7):
                if s[j] != '?' and s[j] != 'abacaba'[j - i]:
                    bad = True
                    break
                s[j] = 'abacaba'[j - i]
            if bad:
                continue
            ans = ''.join(s).replace('?', 'z')
            if count(ans, 'abacaba') == 1:
                good = True
                break
    if good:
        print('Yes')
        print(ans)
    else:
        print('No')
