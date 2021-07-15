N,M = list(map(int,input().split()))
AB = [list(map(int,input().split())) for _ in range(N)]

AB.sort(key= lambda x:(-x[1],-x[0]))#報酬が高く、かつ、振り込みの日数が長いものからやるためのソート
memo = [0]*(10**5+1)#請け負うと決めた仕事の日のメモ。1がついている日は仕事がすでにある
work = [float('inf')]*(10**5+1)#振り込みまでに必要な日数のうち、前回請け負いを決めた日
noMore = float('inf') #これ以上の日数が振り込みにかかる仕事は受けれない
ans = 0
for a,b in AB:
    if a< noMore:#期日までに報酬が受け取れる仕事であること
        flag = 1
        for idx in range(min(M-a,work[a]),-1,-1):#この検索範囲の絞り込みがTLE解消の決め手。前回検索時に請け負った日またはM-a日以前の日
            if memo[idx] == 0:#仕事が請けられる
                ans += b#報酬を足す
                memo[idx]=1#仕事を受けたことの記録。この日はもう受けられない
                flag = 0#noMoreの更新分岐のため
                work[a] = idx#次回検索時のメモ
                break
        if flag ==1:#請けれる日が見つからなければ、今後この日数以上の日は受けれないので調べない
            noMore = a
    
print(ans)
    

