# 入力
N = int(input())

S1 = [] # 増えるシーケンス用
S2 = [] # 減るシーケンス用

# 入力その２
for i in range(N):

    S = input()  # シーケンス
    mid, end = 0, 0    

    for s in S:
        if s == '(':
            end += 1
        else:
            end -= 1
            
        mid = min(mid, end)  # 途中経過で一番減るところを探す

    if end > 0:
        S1.append((mid, end))
    else:
        S2.append((mid-end, -end))

S1.sort(reverse=True)
# S2.sort(key = lambda x : (x[0], -x[1]))
S2.sort(reverse=True)


mid = end1 = 0  # スタート
out = False

for t in S1:
    a, b = t
    mid = end1 + a
    end1 = end1 + b
    if mid < 0:  # 途中で左カッコの数が右を上回る
        out = True
        break

mid = end2 = 0  # スタート
for t in S2:
    a, b = t
    mid = end2 + a
    end2 = end2 + b
    if mid < 0:  # 途中で左カッコの数が右を上回る
        out = True
        break
        
if (not end1 == end2) or out:  # 右、左 の数が合わない
    print('No')
else:
    print('Yes')
