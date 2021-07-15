t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))
    cnt_p0 = 0
    cnt_p1 = 0
    cnt_q0 = 0
    cnt_q1 = 0
    for i in range(n):
        if p[i] % 2 == 0:
            cnt_p0 += 1
        else:
            cnt_p1 += 1
    for i in range(m):
        if q[i] % 2 == 0:
            cnt_q0 += 1
        else:
            cnt_q1 += 1
    print(cnt_p0*cnt_q0 + cnt_p1*cnt_q1)
