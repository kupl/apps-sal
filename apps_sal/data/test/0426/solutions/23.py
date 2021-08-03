n, k = map(int, input().split())
S = list(input())
i = 0
if n == 1:
    if k:
        print(0)
    else:
        print(''.join(S))
else:
    while k:
        if i == n:
            break
        if i == 0:
            if S[i] == '1':
                i += 1
                continue
            else:
                S[i] = '1'
        else:
            if S[i] == '0':
                i += 1
                continue
            else:
                S[i] = '0'
        k -= 1
        i += 1
    print(''.join(S))
