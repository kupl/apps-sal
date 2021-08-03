def main():
    n, k, d = list(map(int, input().split()))
    l = list(map(int, input().split()))
    rez = 0
    rezline = {}
    for i in range(d):
        if rezline.get(l[i]) is None:
            rezline[l[i]] = 0
            rez += 1
        rezline[l[i]] += 1
    rez_p = rez
    for i in range(d, n):
        if rezline[l[i - d]] == 1:
            rez_p -= 1
        rezline[l[i - d]] -= 1
        if rezline.get(l[i]) in [0, None]:
            rez_p += 1
            rezline[l[i]] = 1
        else:
            rezline[l[i]] += 1
        rez = min(rez, rez_p)
    print(rez)


t = int(input())
for i in range(t):
    main()
