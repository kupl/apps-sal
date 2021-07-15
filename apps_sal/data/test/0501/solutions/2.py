def helper(n):
    R = 0
    tmp = n + 1
    while tmp != 1:
        tmp >>= 1
        R += 1
    bottom = R >> 1
    top = R - bottom
    flag = (top > bottom)
    tcnt = 0
    tmp = 1
    while top:
        tcnt += tmp
        tmp <<= 2
        top -= 1
    bcnt = 0
    tmp = 2
    while bottom:
        bcnt += tmp
        tmp <<= 2
        bottom -= 1
    n -= tcnt + bcnt
    if flag:
        bcnt += n
    else:
        tcnt += n
    ans = (pow(tcnt, 2, 1000000007) + (bcnt * (bcnt + 1))) % 1000000007
    return ans
        

def main():
    l, r = map(int, input().split())
    ans = helper(r)
    if l != 1:
        ans -= helper(l - 1)
    print(ans % 1000000007)
    return 0
main()
