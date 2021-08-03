def waru(a, b):
    if a % b == 0:
        return a // b
    else:
        return (a // b) + 1


N, K = map(int, input().split())
A = list(map(int, input().split()))
ue = sum(A)
sita = 1
for i in range(50):
    n = (ue + sita) // 2
    L = [waru(i, n) - 1 for i in A]
    if sum(L) > K:
        sita = n
    else:
        ue = n
    if ue == sita:
        print(ue)
        return
    elif ue - sita == 1:
        n = sita
        L = [waru(i, n) - 1 for i in A]
        if sum(L) > K:
            print(n + 1)
            return
        else:
            print(n)
            return
