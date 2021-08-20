check = 'abacaba'


def compare(s, t):
    res = True
    for i in range(len(s)):
        res &= s[i] == t[i] or s[i] == '?' or t[i] == '?'
    return res


for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 'No'
    res = ''
    for i in range(n - 6):
        t = s
        test = t[i:i + 7]
        if compare(test, check):
            t = s[:i] + check + s[i + 7:]
            t = t.replace('?', 'z')
            count = 0
            for j in range(n - 6):
                if t[j:j + 7] == check:
                    count += 1
            if count == 1:
                ans = 'Yes'
                res = t
    print(ans)
    if ans == 'Yes':
        print(res)
