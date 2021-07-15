
def __starting_point():
    h, w = list(map(int, input().split()))
    s = []
    for _ in range(h):
        s.append(list(input()))

    rr, cc = None, None

    for r in range(1, h-1):
        for c in range(1, w - 1):
            if s[r][c] == s[r-1][c] == s[r][c-1] == s[r+1][c] == s[r][c+1] == '*':
                s[r][c] = '.'

                i = r + 1
                while i < h and s[i][c] == '*':
                    s[i][c] = '.'
                    i += 1

                i = r - 1
                while i >= 0 and s[i][c] == '*':
                    s[i][c] = '.'
                    i -= 1

                i = c + 1
                while i < w and s[r][i] == '*':
                    s[r][i] = '.'
                    i += 1

                i = c - 1
                while i >= 0 and s[r][i] == '*':
                    s[r][i] = '.'
                    i -= 1

                for i in range(h):
                    for j in range(w):
                        if s[i][j] == '*':
                            print("NO")
                            return

                print("YES")
                return

    print("NO")



__starting_point()
