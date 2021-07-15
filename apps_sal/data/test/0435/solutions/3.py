n, k = map(int, input().split())
S = input()

l = r = 0
a = b = 0
ans = 0

while r < n :
    if a <= k or a == 0 or b <= k or b == 0:
        ans = max(ans, r - l)

        if S[r] == 'a' : a += 1
        else : b += 1
        r += 1
    else :
        if S[l] == 'a' : a -= 1
        else : b -= 1
        l += 1

    if a <= k or a == 0 or b <= k or b == 0:
        ans = max(ans, r - l)

print(ans)
