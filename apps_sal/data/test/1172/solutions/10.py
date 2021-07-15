def main():
    mod = 10**9 + 7
    s = input()
    n = len(s)

    a_num = 0
    c_num = s.count('C')
    q_num = 0
    q_cnt = s.count('?')

    pows = [0] * 4
    if q_cnt >= 3:
        pows[3] = pow(3, q_cnt-3, mod)
        pows[2] = pows[3] * 3 % mod
        pows[1] = pows[2] * 3 % mod
        pows[0] = pows[1] * 3 % mod
    elif q_cnt == 2:
        pows[2] = 1
        pows[1] = 3
        pows[0] = 9
    elif q_cnt == 1:
        pows[1] = 1
        pows[0] = 3
    else:
        pows[0] = 1

    ans = 0
    for x in s:
        if x == 'A':
            a_num += 1
        elif x == 'B':
            ans += pows[0] * a_num * c_num
            ans += pows[1] * (q_num * c_num + a_num * (q_cnt - q_num))
            ans += pows[2] * (q_num) * (q_cnt - q_num)
            ans %= mod
        elif x == 'C':
            c_num -= 1
        else:
            ans += pows[1] * a_num * c_num
            ans += pows[2] * (q_num * c_num + a_num * (q_cnt - q_num - 1))
            ans += pows[3] * (q_num) * (q_cnt - q_num - 1)
            ans %= mod
            q_num += 1

    print(ans)

main()
