n = int(input())
t_all, a_all = 0, 0
for i in range(n):
    t, a = list(map(int, input().split()))
    if i == 0:
        t_all = t
        a_all = a
    else:
        if t >= t_all and a >= a_all:
            t_all, a_all = t, a
        else:
            diff1, diff2 = 0, 0
            diff1 = t_all // t if t_all % t == 0 else t_all // t + 1
            diff2 = a_all // a if a_all % a == 0 else a_all // a + 1
            max_diff = max(diff1, diff2)
            t_all = t * max_diff
            a_all = a * max_diff
print((t_all + a_all))
        

