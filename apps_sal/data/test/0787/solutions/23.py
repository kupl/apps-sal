def solve():
    n = int(input())
    s = str(input())

    if n == 1:
        print("YES")
        print(s)
        return

    mp = dict()
    pos = []
    for i, letter in enumerate(s):
        if letter in mp:
            continue
        else:
            mp[letter] = True
            pos.append(i)

    if len(mp) < n:
        print("NO")
    else:
        print("YES")
        start = 0
        for i in range(n - 1):
            print(s[start: pos[i + 1]])
            start = pos[i + 1]
        print(s[start:])

def __starting_point():
    solve()





__starting_point()
