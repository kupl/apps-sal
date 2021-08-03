n = int(input())

for _ in range(n):
    k = int(input())
    s = input()
    s = s[0] + s + str(int(s[-1]) ^ 1)

    m = []

    prev = 1

    for i in range(1, k + 2):
        if s[i] != s[i - 1]:
            m.append(i - prev)
            prev = i

    ans = 0
    start = 0
    end = len(m)
    first = 0

    while (start < end):
        if m[start] > 1:
            start += 1
            first = max(first, start)

        else:
            while (first < end) and (m[first] == 1):
                first += 1

            if (first >= end):
                end -= 1
            else:
                m[first] -= 1

            start += 1

        ans += 1

    print(ans)
