import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
 
N = int(input())

A = [None] * N
# インデックス：-1で先頭にアクセスするため前後反転
# 最初の選手を指す場合０になるように-1した値を保持
# 全組み合わせを試合し終わった時は−１になるようにする
for i in range(N):
    A[i] = [-1] + [int(x) - 1 for x in input().split()[::-1]]


def f(candi):
    
    played = []
    
    # 次に試合する可能性のある選手を順次チェック
    for n in candi:
        target = A[n][-1]
        if A[target][-1] == n:
            played.append(n)
        
    new_candi = set()    
    for n in played:
        # 試合ずみの組み合わせを削除
        A[n].pop()
        # 試合する人の候補に追加
        new_candi.add(n)
        # 次の対戦相手を試合の候補に追加
        if A[n][-1] != -1:
            new_candi.add(A[n][-1])
            
    return len(played), new_candi


answer = 0
# 最悪の試合数（二倍された値）
rest = N*(N-1)
# 試合する人の候補
play_candi = set(range(N))

while True:
    answer += 1
    x, play_candi = f(play_candi)
    # 行われた試合数を確認
    if x == 0:
        answer = -1
        break
        
    rest -= x
    if rest ==0:
        break
        
print(answer)

