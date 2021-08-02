def main():
    n, m = list(map(int, input().split()))
    l = list(map(int, input().split()))
    x = list(map(int, input().split()))
    m = {}
    for i in l:
        for j in x:
            m[(i, j)] = i * j
    c = -99798789896868767678678687687
    for i in m:
        if(m[i] > c):
            c = m[i]
            y = i[0]
    l.remove(y)
    c = -99798789896868767678678687687
    for i in l:
        for j in x:
            c = max(c, i * j)
    print(c)


main()
