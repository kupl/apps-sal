def main():
    #n, m = map(int, input().split())

    n = int(input())
    s = input()
    
    a, b, ans = 0, 0, 0
    cnt = 1
    for i in range(n):
        if s[i] == "?":
            ans = (ans*3 + b) % 1000_000_007
            b = (b * 3 + a) % 1000_000_007
            a = (a * 3 + cnt) % 1000_000_007
            cnt = (cnt * 3) % 1000_000_007
        elif s[i] == "c":
            ans = (ans + b) % 1000_000_007
        elif s[i] == "b":
            b = (b + a) % 1000_000_007
        elif s[i] == "a":
            a = (a + cnt) % 1000_000_007
    print(ans)

#input = sys.stdin.readline

#sys.setrecursionlimit(2097152)
tn = 1 #int(input())
for _ in range(tn):
    main()
