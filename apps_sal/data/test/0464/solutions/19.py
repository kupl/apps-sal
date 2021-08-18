def main():
    h, w = list(map(int, input().split()))
    matrix = [input() for j in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '*':
                cnt += 1
    if w < 3 or h < 3:
        print("NO")
    else:
        ok = False
        for y in range(1, h - 1):
            for x in range(1, w - 1):
                if matrix[y][x] == '*' and matrix[y + 1][x] == '*' and matrix[y - 1][x] == '*' and matrix[y][x + 1] == '*' and matrix[y][x - 1] == '*':
                    r = ""
                    c = ""
                    for i in range(w):
                        r += matrix[y][i]
                    for i in range(h):
                        c += matrix[i][x]
                    subbuff = 0
                    left, right = r.find('*'), r.rfind('*')
                    for i in range(left, right + 1):
                        if r[i] != '*':
                            break
                        else:
                            subbuff += 1
                    if subbuff != right - left + 1:
                        ok = False
                        break
                    buff = 0
                    left, right = c.find('*'), c.rfind('*')
                    for i in range(left, right + 1):
                        if c[i] != '*':
                            break
                        else:
                            buff += 1
                    if buff != right - left + 1:
                        ok = False
                        break
                    if subbuff + buff == cnt + 1:
                        ok = True
                    break
        if ok:
            print("YES")
        else:
            print("NO")


main()
