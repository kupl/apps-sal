for t in range(int(input())):
    p, f = list(map(int, input().split()))
    c_sw, c_ax = list(map(int, input().split()))
    w_sw, w_ax = list(map(int, input().split()))
    
    if w_sw > w_ax:
        c_sw, c_ax = c_ax, c_sw
        w_sw, w_ax = w_ax, w_sw

    ans = 0
    for n_sw_p in range(c_sw + 1):
        n_sw_f = c_sw - n_sw_p

        n_sw_p = min(n_sw_p, p // w_sw)
        n_sw_f = min(n_sw_f, f // w_sw)

        n_ax_p = (p - n_sw_p * w_sw) // w_ax
        n_ax_f = (f - n_sw_f * w_sw) // w_ax

        n_ax = min(n_ax_p + n_ax_f, c_ax)

        ans = max(ans, n_sw_p + n_sw_f + n_ax)
    print(ans)

