from array import array


def popcount(x):
    res = 0
    while(x > 0):
        res += (x & 1)
        x >>= 1
    return res


def main():
    n = int(input())
    a = array('i', [popcount(int(x)) for x in input().split(' ')])

    ans, s0, s1 = 0, 0, 0
    for i in range(n):
        if(a[i] & 1):
            s0, s1 = s1, s0 + 1
        else:
            s0, s1 = s0 + 1, s1
        ans += s0

    for i in range(n):
        mx, sum = a[i], 0
        for j in range(i, min(n, i + 70)):
            mx = max(mx, a[j] << 1)
            sum += a[j]
            if((sum & 1 is 0) and (mx > sum)):
                ans -= 1
    print(ans)


main()
