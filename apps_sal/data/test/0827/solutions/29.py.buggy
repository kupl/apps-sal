N = int(input())
T = input()

if N > 2:
    for i in range(N - 2):
        if int(T[i]) + int(T[i + 1]) + int(T[i + 2]) != 2:
            print((0))
            return
elif T == '00':
    print((0))
    return

if T == '1':
    ans = 2 * 10**10
elif T == '11':
    ans = 10**10
else:
    cnt = T.count('0')
    if T[-1] == '0':
        ans = 10**10 - (cnt - 1)
    else:
        ans = 10**10 - cnt
print(ans)
