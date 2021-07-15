for _ in range(int(input())):
    n = int(input())
    *s, = list(map(int, input()))
    cnt = [0, 0]
    for i in range(len(s)):
        if i > 0 and s[i] == s[i - 1]:
            cnt[s[i]] += 1
    print(max(cnt))



