(N, K) = map(int, input().split())
Alist = list(map(int, input().split()))
Slist = [0]
tale = N + 1
for i in range(N):
    try:
        S += Alist[i]
    except:
        S = Alist[i]
    Slist.append(S)
    if S >= K and tale == N + 1:
        tale = i + 1
Ans = N - tale + 1
if Ans != 0:
    for head in range(1, N + 1):
        Sum = Slist[tale] - Slist[head]
        if Sum >= K:
            Ans += N - tale + 1
        elif tale == head and tale < N:
            for _ in range(10 ** 6):
                tale += 1
                Sum = Slist[tale] - Slist[head]
                if Sum >= K:
                    Ans += N - tale + 1
                    break
                elif tale == N:
                    break
        elif tale != N:
            for _ in range(10 ** 6):
                tale += 1
                Sum = Slist[tale] - Slist[head]
                if Sum >= K:
                    Ans += N - tale + 1
                    break
                elif tale == N:
                    break
        if tale > N:
            break
print(Ans)
