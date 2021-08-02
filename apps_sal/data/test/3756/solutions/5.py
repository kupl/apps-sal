def main():
    n, t = list(map(int, input().split()))
    b = list(input())
    p = b.index('.')

    if int(b[p + 1]) > 4:
        del b[p:n]
        b = list(b)
        for x in range(len(b) - 1, -1, -1):
            if b[x] == '9':
                b[x] = '0'
            else:
                b[x] = chr(ord(b[x]) + 1)
                break
        else:
            b.insert(0, '1')
        print(''.join(b))
        return
    else:
        if p + 1 < n - 1:
            for x in range(p + 1, n):
                if int(b[x + 1]) > 4:
                    b[x] = chr(ord(b[x]) + 1)
                    del b[x + 1:n]
                    t -= 1
                    break
            else:
                print(''.join(b))
                return
            for y in range(x, p, -1):
                if int(b[y]) < 5 or t == 0:
                    break
                elif b[y - 1] != '.':
                    b[y - 1] = str(int(b[y - 1]) + 1)
                    del b[y:n]
                    t -= 1
                elif b[y - 1] == '.':
                    del b[y - 1:n]
                    b = list(b)
                    for x in range(len(b) - 1, -1, -1):
                        if b[x] == '9':
                            b[x] = '0'
                        else:
                            b[x] = chr(ord(b[x]) + 1)
                            break
                    else:
                        b.insert(0, '1')
        b = ''.join(b)
    print(b)


main()
