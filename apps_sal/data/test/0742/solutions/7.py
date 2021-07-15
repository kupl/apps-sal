t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    m = [1 for j in range(2 * n)]
    for k in b:
        m[k - 1] = 0
    a = []
    mega_bul = True
    for el in b:
        a.append(el)
        ind = 0
        bul = False
        while ind < 2 * n:
            if ind + 1 > el and m[ind] == 1:
                m[ind] = 0
                a.append(ind + 1)
                bul = True
                break
            ind += 1
        if not bul:
            mega_bul = False
            break
    if mega_bul:
        print(" ".join(map(str, a)))
    else:
        print(-1)

