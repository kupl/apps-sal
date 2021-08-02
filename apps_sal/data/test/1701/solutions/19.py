

def main():
    n, m = list(map(int, input().split()))
    d = dict()
    for i in range(n):
        name, ip = input().split()
        d[ip] = name

    for i in range(m):
        s = input()
        com, ip = s.split()
        ip = ip.strip(';')
        print(s + ' #' + d[ip])


main()
