N = int(input())
N_List = sorted(list(map(int, input().split())))
flg = 0
ans = 1
if N % 2 == 1:
    if N_List[0] != 0:
        flg = 1
    else:
        for i in range(2, N, 2):
            if i * 2 != sum(N_List[i - 1:i + 1]):
                flg = 1
                break
            else:
                ans = ans * 2 % (10 ** 9 + 7)
else:
    for i in range(1, N, 2):
        if i * 2 != sum(N_List[i - 1:i + 1]):
            flg = 1
            break
        else:
            ans = ans * 2 % (10 ** 9 + 7)
if flg == 0:
    print(ans)
else:
    print(0)
