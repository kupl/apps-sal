import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    H,W,K = map(int, readline().split())
    S = [list(map(int, readline().strip())) for j in range(H)]
    
    white = 0
    for line in S:
        white += sum(line)
 
    if white <= K:
        print(0)
        return
 
    # 横線の決め方を全探索
    ans = 10**5
    
    #yに横線Patternごとの列合計を作成
    #入力例１のPattern[bin(2)]場合、y=[[1,1,1,0,0], [1,0,1,1,2]]
    for pattern in range(2**(H-1)):
        # 初期化
        impossible = False
        x = 0
        ly = bin(pattern).count("1")
        y = [S[0]]
        line = 0
        for i in range(1,H):
            if (pattern >> i-1) & 1:
                line += 1
                y.append(S[i])
            else:
                y[line] = [y[line][j] + S[i][j] for j in range(W)]
 
        # 各列の値を加算していく
        count = [0]*(ly + 1) 
        for j in range(W):
            for i in range(line+1):
                if y[i][j] > K :
                    impossible = True
                    break
 
                count[i] += y[i][j]
                #print("横Pattern{} 縦列まで　{} カウント数{} 縦線の数{}".format(i, j, count[i], x))
                #横Patten毎にｊ列までのホワイトチョコ合計数をカウント、
                #カウント＞Kとなったら、縦線数を＋１、その列値でカウント数を初期化
                if count[i] > K:
                    x += 1
                    for i in range(line+1):
                        count[i] = y[i][j]
                    break
            #x縦線の数 + ly横線の数がAnsより大きくなったらBreak
            if x + ly > ans or impossible:
                impossible = True
                break
        if impossible:
            x = 10**6
        #x縦線の数 + ly横線の数がAnsより小さくなったらAnsを更新
        ans = min(ans, x + ly)
 
    print(ans)
 
 
main()
