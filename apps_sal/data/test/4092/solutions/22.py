def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = {0}
    acc = 0
    ans = 0
    for x in a:
        acc += x
        if acc in s:
            ans += 1
            s = {0, x}
            acc = x
        else:
            s.add(acc)
    print(ans)


tn = 1
for _ in range(tn):
    main()
