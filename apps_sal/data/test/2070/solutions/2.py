def solve(left, right) :
    if left == right :
        return 0
    if left+1 == right :
        return 0
    mid = (left+right)//2
    ret = solve(left, mid) + solve(mid, right)
    val = 0
    D = [dict() for i in range(26)]
    for i in range(mid, right) :
        c = L[i]
        if i != mid :            
            d = L[i-1]
            val += A[d]
        if val in D[c] : D[c][val] += 1
        else : D[c][val] = 1
    val = 0
    for i in range(mid, left, -1) :
        c = L[i-1]
        if i != mid :
            d = L[i]
            val += A[d]
        if -val in D[c] :
            ret += D[c][-val]
    return ret

A = list(map(int, input().split()))
S = input()
L = [ord(i)-ord('a') for i in S]

ans = solve(0, len(L))
print(ans)

