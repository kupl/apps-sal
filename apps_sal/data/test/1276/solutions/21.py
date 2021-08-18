
def main():
    '''
    n = int(input())
    s = input()
    cnt = 0
    for i in range(len(s)):
        x = s[i]
        for j in range(i+1, len(s)):
            y = s[j]
            if x == y:
                continue
            for k in range(j+1, len(s)):
                z = s[k]
                if z == x or z == y:
                    continue
                if j - i == k - j:
                    continue
                cnt += 1
    print(cnt)
    '''
    n = int(input())
    s = input()
    cnt = [0] * 3
    ans = 1
    for i in s:
        if i == 'R':
            cnt[0] += 1
        elif i == 'G':
            cnt[1] += 1
        else:
            cnt[2] += 1
    for i in cnt:
        ans *= i
    for i in range(n):
        for j in range(i + 1, n):
            k = j + (j - i)
            if k < n:
                if s[i] == s[j]:
                    continue
                if s[j] == s[k]:
                    continue
                if s[k] == s[i]:
                    continue
                ans -= 1
    print(ans)


def __starting_point():
    main()


__starting_point()
