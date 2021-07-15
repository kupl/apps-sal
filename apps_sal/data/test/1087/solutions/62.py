def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    digit = len(str(bin(K)))-2
    digits1 = [0]*digit
    ans = 0
    for a in A:
        ans += a-a%(1<<digit)
        for i in range(digit):
            if a&1<<i:
                digits1[i] += 1
    x = 0
    for i in range(digit-1,-1,-1):
        if digits1[i]<N/2 and x+(1<<i) <=K:
            x += 1<<i
            ans += (1<<i)*(N-digits1[i])
        else:
            ans += (1<<i)*digits1[i]
    return ans
print(solve())
