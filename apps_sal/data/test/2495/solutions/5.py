N = int(input())
A = list(map(int, input().split()))


def calc(a, t):
    ans = 0
    p_flag = t < 0
    t += a
    if p_flag:
        if t < 0:
            ans = 1 - t
            t = 1
    else:
        if t >= 0:
            ans = 1 + t
            t = -1
    if t == 0:
        ans += 1
        if p_flag:
            t = 1
        else:
            t = -1

    return ans, t


ans_p = 0
t_p = 0
ans_m = 0
t_m = 0
if A[0] > 0:
    ans_p = 0
    t_p = A[0]
    ans_m = A[0] + 1
    t_m = -1
elif A[0] < 0:
    ans_p = -A[0] + 1
    t_p = 1
    ans_m = 0
    t_m = A[0]
else:
    ans_p = 1
    t_p = 1
    ans_m = 1
    t_m = -1

for i in range(1, N):
    a, t_p = calc(A[i], t_p)
    ans_p += a
    a, t_m = calc(A[i], t_m)
    ans_m += a

print((min(ans_p, ans_m)))
