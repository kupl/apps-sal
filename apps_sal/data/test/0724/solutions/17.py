from sys import stdin as cin


def main():
    (n, m) = list(map(int, cin.readline().split()))
    a = list(map(int, cin.readline().split()))
    a.sort()
    x = 0
    y = -1
    for i in range(n):
        if a[i] - a[0] > m:
            y = i
            break
    if y == -1:
        print(0)
        return
    o = n - y
    while y < n:
        x += 1
        while y < n and a[y] - a[x] <= m:
            y += 1
        o = min(n - y + x, o)
    print(o)


main()
