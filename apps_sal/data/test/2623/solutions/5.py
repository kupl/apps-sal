q = int(input())
for _ in range(q):
    n, k = list(map(int, input().split()))
    s = list(input())
    s.sort()
    slowo = [[] for i in range(k)]
    if s[0] != s[k - 1]:
        print(s[k - 1])
    else:
        if k == n:
            print(s[n - 1])
        else:
            dl = (n - 1) // k
            if s[k] == s[-1]:
                odp = [s[0]] + [s[k]] * dl
            else:
                odp = [s[0]] + s[k:]
            print("".join(odp))
