N, M = map(int, input().split())

if N%2:
    for i in range(M):
        print(2+i, N-i)
else:
    used = set()
    s = 1
    for i in list(range(2, M+1, 2)[::-1])+list(range(1, M+1, 2)[::-1]):
        while 1:
            if not s in used and not (s+i) in used:
                used.add(s)
                used.add(s+i)
                print(s, s+i)
                break
            s += 1
