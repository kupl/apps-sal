N, K = list(map(int, input().split()))
a = [int(i) for i in input().split()]
N = {4: N, 3: 0, 2: N * 2, 1: 0}

works = True
a.sort(reverse=True)

for i in range(K):
    r4 = min(N[4], a[i] // 4)
    a[i] -= 4 * r4
    N[4] -= r4

a.sort(reverse=True)
# print(a,N)
for i in range(K):
    if a[i] == 0:
        continue
    r2 = min(N[2], a[i] // 2)
    a[i] -= 2 * r2
    N[2] -= r2

a.sort(reverse=True)
# print(a,N)
for i in range(K):
    # print("a",a,N,a[i])
    if a[i] == 0:
        continue
    if a[i] >= 4:
        works = False
        break
    # print("x")
    if a[i] == 3:
        #print(" ai is 3")
        x = min(N[4], 1)
        a[i] -= 3 * x
        N[4] -= x

    elif a[i] == 2:
        #print( "ai is 2")
        x = min(N[2], a[i] // 2)
        a[i] -= 2 * x
        N[2] -= x

        x = min(N[4], a[i] // 2)
        a[i] -= 2 * x
        N[4] -= x
        N[1] += x

        x = min(N[1], a[i])
        a[i] -= x
        N[1] -= x

    elif a[i] == 1:
        #print(" ai is 1")
        N[1] += N[2]
        N[1] += 2 * N[4]
        N[4] = 0
        N[2] = 0

        x = min(N[1], a[i])
        a[i] -= x
        N[1] -= x

    if a[i] != 0:
        # print(a[i])
        works = False
        break


if works:
    print("YES")
else:
    print("NO")
