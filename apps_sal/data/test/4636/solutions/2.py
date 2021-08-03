for t in range(int(input())):
    n = int(input())
    cand = list(map(int, input().split()))
    a = 0
    b = 0
    i = 0
    j = n - 1
    prev = 0
    moves = 0
    while i <= j:
        curr = 0
        while i <= j and curr <= prev:
            curr += cand[i]
            i += 1
        a += curr
        prev = curr
        moves += bool(curr)
        curr = 0
        while i <= j and curr <= prev:
            curr += cand[j]
            j -= 1
        b += curr
        prev = curr
        moves += bool(curr)
    print(moves, a, b)
