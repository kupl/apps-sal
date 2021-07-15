def __starting_point():

    n,m,a = list(map(int,input().split()))

    A = []
    for i in range(n):
        cmd = list(map(int,input().split()))
        A.append(cmd)
    #bit全探索 買う・買わないを判断する
    INF = 10**19
    ans = INF
    for x in range(2**n):
        ALG = [0]*m
        gokei = 0
        for y in range(n):
            if (x>>y) & 1:
                #取得する配列が決まったら、アルゴリズム理解度を＋していく
                for j in range(m):
                    ALG[j] += A[y][j+1]
                gokei += A[y][0]
        #Alg配列の中身がすべて理解度xを超えているかのチェック
        algflg=True
        for k in ALG:
            if k < a:
                algflg=False
                break
        if algflg:
            ans = min(ans,gokei)
    if ans == INF:
        print("-1")
    else:
        print(ans)

__starting_point()
