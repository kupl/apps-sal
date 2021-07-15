N = int(input())
T = input()

max_num = len(T)//3 + 2
if max_num >= 10**10:
    max_num = 10**10
check = '110' * max_num
if T not in check:
    print((0))
    return
elif N == 1 and T[0] == '1':
    print((2*10**10))
    return
else:
    cnt = 0
    for i in range(len(T)):
        if T[i] == '0':
            cnt += 1
    if T[-1] != '0':
        cnt += 1
ans = 10**10 - cnt + 1
print(ans)

