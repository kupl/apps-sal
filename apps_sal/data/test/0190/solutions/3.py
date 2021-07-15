def main():
    n, m = list(map(int, input().split()))
    x1, y1, x2, y2 = n, m, -1, -1
    for i in range(n):
        s = input()
        for j in range(m):
            if s[j] == '*':
                x1, y1 = min(i, x1), min(j, y1)
                x2, y2 = max(i, x2), max(j, y2)
    ans = max(x2 - x1, y2 - y1) + 1
    print(ans)
main()

