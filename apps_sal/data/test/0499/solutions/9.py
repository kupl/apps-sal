def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    if r > 0 and g > 0 and b > 0:
        print('BGR')
        return
    r = min(r, 2)
    g = min(g, 2)
    b = min(b, 2)
    a = r, 'R'
    c = b, 'B'
    b = g, 'G'
    if a[0] < b[0]:
        a, b = b, a
    if b[0] < c[0]:
        b, c = c, b
    if a[0] < b[0]:
        a, b = b, a
    if a[0] == 2 and b[0] == 2:
        print('BGR')
        return
    if a[0] == 2 and b[0] == 1:
        print(''.join(sorted((c[1], b[1]))))
    if a[0] > 0 and b[0] == 0:
        print(a[1])
    if a[0] == 1 and b[0] == 1:
        print(c[1])


main()

