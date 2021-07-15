def main():
    #n, m = map(int, input().split())
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

#input = sys.stdin.readline

#sys.setrecursionlimit(2097152)
tn = 1 #int(input())
for _ in range(tn):
    main()
