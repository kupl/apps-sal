#愚直回 ３重ループ 30x30x30x500x500=6.75*10**9 厳しいか。。。
#メモ化しとけばいける？-->python TLE, pypy3 262ms #17206796
#出現するものをカウントしておく
memo_mod = [[-1]*31 for _ in range(3)]
memo_app = [[0]*31 for _ in range(3)]

N,C = list(map(int,input().split()))
D = [list(map(int,input().split())) for _ in range(C)]
c = [list(map(int,input().split())) for _ in range(N)]
fa=float('inf')

for i in range(N):
    for j in range(N):
        memo_app[(i+j)%3][c[i][j]] +=1

for mod0 in range(1,C+1):
    for mod1 in range(1,C+1):
        for mod2 in range(1,C+1):
            if mod0 == mod1 or mod1==mod2 or mod2==mod0:
                continue
            else:
                ans = 0
                if memo_mod[0][mod0]== -1:
                    tmp = 0
                    for idx in range(1,C+1):
                        tmp += memo_app[0][idx]*D[idx-1][mod0-1]
                    ans += tmp
                else:
                    ans += memo_mod[0][mod0]

                if memo_mod[1][mod1]== -1:
                    tmp = 0
                    for idx in range(1,C+1):
                        tmp += memo_app[1][idx]*D[idx-1][mod1-1]
                    ans += tmp
                else:
                    ans += memo_mod[1][mod1]


                if memo_mod[2][mod2]== -1:
                    tmp = 0
                    for idx in range(1,C+1):
                        tmp += memo_app[2][idx]*D[idx-1][mod2-1]
                    ans += tmp
                else:
                    ans += memo_mod[2][mod2]
                fa = min(fa,ans)
print(fa)

