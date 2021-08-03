N = int(input())
A = list(map(int, input().split()))

ans = 0
w_xor, w_sum = A[0], A[0]
l, r = 0, 0

while l < N and r < N:
    #print(l,r,w_xor, w_sum)

    if w_xor == w_sum:
        if r < N - 1:
            # print(l,r)
            r += 1
            w_xor = w_xor ^ A[r]
            w_sum = w_sum + A[r]
            continue
        else:
            ans += 1 + r - l
    else:
        # l,r-1、までがマッチしてたということなので1小さい
        ans += r - l
    w_xor = w_xor ^ A[l]
    w_sum = w_sum - A[l]
    l += 1

print(ans)
