t = int(input())


c = [0] * 200100
for _ in range(t):
    s = input()
    for i in range(len(s)):
        c[i] = s[i] == '0'
        if i and s[i] == '0':
            c[i] += c[i - 1]

    sol = 0
    for i in range(len(s)):
        tmp = 0
        for k in range(20):
            if i - k < 0:
                break

            tmp += (s[i - k] == '1') << k
            if tmp == k + 1:
                sol += 1

        if i >= 20:
            top = 20 + c[i - 20]
            if tmp > 20 and tmp <= top:
                sol += 1
    print(sol)
