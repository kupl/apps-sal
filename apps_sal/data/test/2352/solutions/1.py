import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    mar = [-1] * 26
    mir = [2000] * 26
    mac = [-1] * 26
    mic = [2000] * 26
    
    X = [[-1 if a == "." else ord(a)-97 for a in input()] for i in range(N)]
    R = [[a+1 for a in range(M)] for _ in range(N)]
    D = [[i+1]*M for i in range(N)]
    
    # print(X)
    ma = -1
    for i in range(N):
        for j in range(M):
            k = X[i][j]
            if k >= 0:
                mar[k] = max(mar[k], i)
                mir[k] = min(mir[k], i)
                mac[k] = max(mac[k], j)
                mic[k] = min(mic[k], j)
                ma = max(ma, k)
    f = 0
    ans = 1
    ANS = []
    for k in range(ma+1)[::-1]:
        if f and mar[k] == -1 and mir[k] == 2000:
            ANS.append(ANS[-1])
        elif mar[k] == mir[k]:
            r = mar[k]
            c = mic[k]
            while c <= mac[k]:
                if X[r][c] < k:
                    ans = 0
                    break
                c = R[r][c]
            else:
                ANS.append((r+1, mic[k]+1, r+1, mac[k]+1))
            R[r][mic[k]] = mac[k] + 1
            if ans == 0:
                break
            f = 1
        elif mac[k] == mic[k]:
            c = mac[k]
            r = mir[k]
            while r <= mar[k]:
                if X[r][c] < k:
                    ans = 0
                    break
                r = D[r][c]
            else:
                ANS.append((mir[k]+1, c+1, mar[k]+1, c+1))
            D[mir[k]][c] = mar[k] + 1
            if ans == 0:
                break
            f = 1
        else:
            ans = 0
            break
    if ans == 0:
        print("NO")
    else:
        print("YES")
        print(len(ANS))
        for a in ANS[::-1]:
            print(*a)

