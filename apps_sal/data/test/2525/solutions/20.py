def main():
    S = list(input())
    T = []
    reverse = False
    n_q = int(input())
    for i in range(n_q):
        q = input().split(' ')
        if q[0] == '1':
            reverse = not reverse
        elif q[0] == '2':
            f = q[1]
            c = q[2]
            if f == '1' and (not reverse) or (f == '2' and reverse):
                T.append(c)
            elif f == '1' and reverse or (f == '2' and (not reverse)):
                S.append(c)
    if reverse:
        S.reverse()
        ans = S + T
    elif not reverse:
        T.reverse()
        ans = T + S
    print(''.join(ans))


main()
