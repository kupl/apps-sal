import math


def nextfront(i, N, T):
    div = T[i]
    for j in range(i + 1, N):
        div = math.gcd(div, T[j])
        if div == 1:
            return j
    return -1


def nextback(k, N, T):
    div = T[k]
    for j in range(k - 1, -1):
        div = math.gcd(div, T[j])
        if div == 1:
            return j
    return -1


def qtduns(T, N):
    resp = 0
    for i in range(N):
        if T[i] == 1:
            resp += 1
    return resp


def main():
    N = int(input())
    T = [int(i) for i in input().split()]
    x = qtduns(T, N)
    if x > 0:
        print(N - x)
        return
    l = N + 1
    i = 0
    k = N + 1
    flag = False
    while i != N and l != 2:
        #print(i, k, l)
        div = T[i]
        for j in range(i + 1, N):
            div = math.gcd(div, T[j])
            if div == 1:
                l = min(l, j - i + 1)
                k = j
                #print(" ", i, j, l)
                break
        if div != 1:
            flag = True
            k = N - 1
        div = T[k]
        for j in range(k - 1, i - 1):
            div = math.gcd(div, T[j])
            if div == 1:
                l = min(l, k - j + 1)
                #print("  ", j, k, l)
                break
        if flag:
            break
        else:
            i = k - l + 2
    if l == N + 1:
        print(-1)
    else:
        print(N + l - 2)


main()

# 1511548364391
