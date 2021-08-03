t = int(input())
for r in range(t):
    n, k = list(map(int, input().split()))
    k -= 1
    want = '()' * k + '(' * (n // 2 - k) + ')' * (n // 2 - k)
    have = input()
    prn = []
    for w in range(len(want)):
        if have[w] != want[w]:
            e = w + have[w:].index(want[w])
            have = have[:w] + have[w:e + 1][::-1] + have[e + 1:]
            prn += [[w + 1, e + 1]]
    print(len(prn))
    for w in prn:
        print(*w)
