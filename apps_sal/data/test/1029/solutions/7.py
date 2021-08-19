3


def main():
    s = input()
    n = len(s)
    if n == 1:
        return 1
    fst = 1
    if int(s[0]) < int(s[1]):
        fst = 2
    ans = 1
    j = 1
    while j < n and s[j] == '0':
        j += 1
    if j == n:
        return 1
    cur = 1
    for i in range(j + 1, n + 1):
        if i == n or s[i] != '0':
            if i - cur < cur or (i - cur == cur and int(s[0]) < int(s[i - cur])):
                ans = 1
            else:
                ans += 1
            cur = 1
        else:
            cur += 1
    return ans


print(main())
