# F問題
N = int(input())
S = list(map(int, input().split()))
S.sort(reverse=True)
visit = [0] * (2**N)
visit[0] = 1
used = [S[0]]

flag = 0
for i in range(N):
    add = used[::-1]
    k = 0
    for u in used:
        while k < 2**N:
            if visit[k] == 0 and S[k] < u:
                visit[k] = 1
                add.append(S[k])
                break
            k += 1
        if k >= 2**N:
            print("No")
            flag = 1
            break
    if flag == 1:
        break

    used = add[::-1]
    used.sort(reverse=True)

if flag == 0:
    print("Yes")
