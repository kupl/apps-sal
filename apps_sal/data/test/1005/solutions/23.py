def main():
    (n, k, d) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    rez = d
    for i in range(n - d + 1):
        rez = min(rez, len(set(l[i:i + d])))
    print(rez)


t = int(input())
for i in range(t):
    main()
