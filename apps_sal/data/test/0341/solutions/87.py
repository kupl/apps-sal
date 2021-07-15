N, K = list(map(int, input().split()))
R, S, P = list(map(int, input().split()))
T = input()

ans = 0
for i in range(0, K):
    rsp_K = T[i::K]
    rsp_before = ''
    for rsp in rsp_K:
        if rsp == 'r':
            if rsp_before != 'r':
                ans += P
                rsp_before = 'r'
            else:
                rsp_before = ''
        elif rsp == 's':
            if rsp_before != 's':
                ans += R
                rsp_before = 's'
            else:
                rsp_before = ''
        elif rsp == 'p':
            if rsp_before != 'p':
                ans += S
                rsp_before = 'p'
            else:
                rsp_before = ''

print(ans)

