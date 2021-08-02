n = int(input())
s = list(input())
cur = 'X'
start, end = 0, 0
i = 0
ans = 0
while i < n:
    if s[i] != cur:
        cur = s[i]
        start = i
        while i < n and s[i] == cur:
            i += 1
        if i == n:
            for ch in 'RBG':
                if ch != s[start]:
                    use = ch
                    break
        else:
            for ch in 'RBG':
                if ch != s[start] and ch != s[i]:
                    use = ch
                    break
        end = i - 1
        for j in range(start, end + 1):
            if (j - start) % 2:
                s[j] = use
                ans += 1
print(ans)
print(''.join(s))
