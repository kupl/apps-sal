Q = int(input())

for _ in range(Q):
    N = int(input())
    s = input()
    mi = N - 1
    for i in range(N):
        if s[i] == ">":
            mi = i
            break
    for i in range(N):
        if s[N-1-i] == "<":
            mi = min(mi, i)
            break

    print(mi)

