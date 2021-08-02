N = int(input())
T = 1
A = 1
for i in range(N):
    Tk = [0, 0]
    Ak = [0, 0]
    Tn, An = map(int, input().rstrip().split(" "))
    if T % Tn == 0:
        Tk[0] = T
    else:
        Tk[0] = (T // Tn + 1) * Tn
    Ak[0] = (Tk[0] // Tn) * An
    if Ak[0] < A:
        Ak[0] = 10 ** 18 + 1

    if A % An == 0:
        Ak[1] = A
    else:
        Ak[1] = (A // An + 1) * An
    Tk[1] = (Ak[1] // An) * Tn
    if Tk[1] < T:
        Tk[1] = 10 ** 18 + 1

    if Tk[0] + Ak[0] <= Tk[1] + Ak[1]:
        T = Tk[0]
        A = Ak[0]
    else:
        T = Tk[1]
        A = Ak[1]
print(A + T)
