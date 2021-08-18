q = int(input())
B = []
OTVET = []
for m in range(q):
    n, k = list(map(int, input().split()))
    sttr = list(map(int, input().split()))
    a = list(sttr)
    kolvo = 0
    nechet = []
    for i in range(n):
        if a[i] % 2 == 1:
            kolvo += 1
            nechet.append(i + 1)
    if (kolvo >= k) and ((kolvo - k) % 2 == 0):
        otsh = []
        for i in range(k - 1):
            otsh.append(nechet[i])
        otsh.append(n)
        B.append(1)
        OTVET.append(otsh)
    else:
        B.append(0)
j = 0
for i in range(q):
    if B[i] == 1:
        print("YES")
        print(*OTVET[j])
        j += 1
    else:
        print("NO")
