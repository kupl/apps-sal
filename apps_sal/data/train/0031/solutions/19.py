t = int(input())
for _ in range(t):
    s = input()
    st = set()
    (x, y) = (0, 0)
    ans = 0
    for c in s:
        if c == 'S':
            if (x, y + 1) in st:
                ans += 1
            else:
                ans += 5
                st.add((x, y + 1))
            y += 2
        elif c == 'N':
            if (x, y - 1) in st:
                ans += 1
            else:
                ans += 5
                st.add((x, y - 1))
            y -= 2
        elif c == 'W':
            if (x + 1, y) in st:
                ans += 1
            else:
                ans += 5
                st.add((x + 1, y))
            x += 2
        else:
            if (x - 1, y) in st:
                ans += 1
            else:
                ans += 5
                st.add((x - 1, y))
            x -= 2
    print(ans)
