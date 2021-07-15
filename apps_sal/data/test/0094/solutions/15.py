def main():
    QWE = 'trick'
    INF = 10 ** 18 + 9
    EPS = 10 ** -7

    import sys, math
    #fi = open('input.txt', 'r')
    #fo = open('output.txt', 'w+')
    #fi = open(QWE +".in", "r")
    #fo = open(QWE + ".out", "w+")
    
    n = input()
    ln = len(n)
    n = int(n);
    s = input()
    m = len(s)
    d = [0] * (m + 1)
    for i in range(1, m + 1):
        d[i] = INF
        for j in range(max(1, i - ln), i + 1):
            if s[j - 1] != '0' or j == i:
                q = int(s[j - 1: i])
                if q < n:
                    d[i] = min(d[i], d[j - 1] * n + q)
    print(d[m])
    #print(d)

main()

