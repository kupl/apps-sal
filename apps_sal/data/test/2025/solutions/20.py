def shis(k):
    if ((k % 2) == 0 and k > 2):
        return(k // 4)
    elif (((k % 2) == 1 and (k >= 13)) or k == 9):
        return((k - 9) // 4 + 1)
    else:
        return(-1)


m1 = []
n = int(input())
for i in range(n):
    m1.append(int(input()))
for i in range(n):
    print(shis(m1[i]))
