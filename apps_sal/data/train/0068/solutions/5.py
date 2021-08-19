T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    arr = []
    seq = 1
    for (a, b) in zip(S, S[1:]):
        if a == b:
            seq += 1
        else:
            arr.append(seq)
            seq = 1
    arr.append(seq)
    hist = []
    arr.reverse()
    for (i, a) in enumerate(arr):
        if a == 1:
            continue
        hist.append([i, a])
    ans = 0
    while len(arr):
        if len(hist):
            hist[-1][1] -= 1
            if hist[-1][1] == 1:
                hist.pop()
        elif len(arr):
            arr.pop()
        else:
            break
        ans += 1
        if len(arr):
            arr.pop()
        if len(hist) and hist[-1][0] == len(arr):
            hist.pop()
    print(ans)
