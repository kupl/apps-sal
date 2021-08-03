t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    try:
        s = s[s.index('8')::]
        if len(s) < 11:
            raise ValueError
        print("YES")
    except ValueError:
        print("NO")
