def judge(A, x, k):
    ans = 0
    for a in A:
        ans += a // x
        if a % x == 0:
            ans -= 1
        if ans > k:
            return False
    return True

n, k = map(int, input().split())
A = list(map(int, input().split()))
l = 0
r = max(A)
while r - l != 1:
    x = (r + l) // 2
    if judge(A, x, k):
        r = x
    else:
        l = x
print(r)
