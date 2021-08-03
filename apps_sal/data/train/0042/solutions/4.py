for _ in range(int(input())):
    s = input()
    q1 = ans = 0
    for q in range(len(s)):
        if s[q] == '0':
            q1 += 1
        else:
            ans += 1 + (q != len(s) - 1 and s[q + 1] == '0')
            q2 = size = 1
            for q3 in range(1, q1 + 1):
                size += 1
                if q2 == size:
                    ans += 1
                while q2 < size and size - q3 + q < len(s):
                    q2 *= 2
                    q2 += ord(s[q + size - q3]) - ord('0')
                    size += 1
                    if q2 == size:
                        ans += 1
            q1 = 0
    print(ans)
