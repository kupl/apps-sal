q = int(input())
for i in range(q):
    s = input()
    L = list(s)
    L.sort()

    for j in range(len(L)):
        if ord(L[j]) == ord(L[0]) + j:
            continue
        else:
            print("No")
            break

    else:
        print("Yes")
