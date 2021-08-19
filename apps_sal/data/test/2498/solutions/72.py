def main():
    N, M = map(int, input().split())
    A = tuple(map(int, input().split()))
    ans = count(A, N, M)
    print(ans)


def count(A, N, M):
    t = hMt(A[0])
    B = [A[0] // (2**t)]
    for val in A[1:]:
        if hMt(val) != t:
            ans = 0
            return ans
        B.append(val // (2**t))
    T = nlcm(B)
    MdivT = (M // (2**(t - 1))) // T
    ans = countodd(MdivT)
    return ans


def countodd(num):
    if num % 2 == 0:
        ans = num // 2
    else:
        ans = num // 2 + num % 2
    return ans


def nlcm(A):
    LCM = A[0]
    for val in A[1:]:
        #print("%d %d gcm:%d LCM:%d"%(LCM,val,gcm(LCM,val),lcm(LCM,val)))
        LCM = lcm(LCM, val)
    return LCM


def gcm(a, b):
    abtuple = (a, b)
    abmin = min([0, 1], key=lambda x: abtuple[x])
    remainder = abtuple[1 - abmin] % abtuple[abmin]
    if remainder == 0:
        return abtuple[abmin]
    return gcm(abtuple[abmin], remainder)


def lcm(a, b):
    prod = a * b
    ans = prod // gcm(a, b)
    return ans


def hMt(num):
    ans = 0
    tmp = num
    while tmp % 2 == 0:
        tmp = tmp // 2
        ans += 1
    return ans


main()
