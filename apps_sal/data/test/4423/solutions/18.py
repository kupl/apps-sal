N = int(input())
Rest = dict()
Parg = [0] * 101
for i in range(N):
    (S, P) = map(str, input().split())
    P = int(P)
    if S not in Rest:
        Rest[S] = [P]
    else:
        Rest[S] += [P]
    Parg[P] = i + 1
Restsort = sorted(Rest)
for cit in Restsort:
    box = Rest[cit]
    box.sort(reverse=True)
    for j in box:
        print(Parg[j])
