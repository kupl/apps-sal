def ans(k):
    arry = [None] * k
    arry[0] = 7 % k
    for i in range(k - 1):
        arry[i+1] = (10*arry[i]+7) % k

    for i in range(k):
        if arry[i] == 0:
            return i+1

    return -1


K = int(input())
print(ans(K))
