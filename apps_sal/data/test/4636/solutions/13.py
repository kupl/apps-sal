for f in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    j = n - 1
    alice = 0
    bob = 0
    prev = 0
    turn = 0
    k = 0
    while i <= j:
        cur = 0
        if turn == 0:
            while cur <= prev and i <= j:
                alice += a[i]
                cur += a[i]
                i += 1
        else:
            while cur <= prev and i <= j:
                bob += a[j]
                cur += a[j]
                j -= 1
        k += 1
        turn = 1 - turn
        prev = cur
    print(k, alice, bob)
