N, K, C = list(map(int,input().split()))
s = list(str(input()))

L = []  # i+1日目に働くのはL[i]日目以降
R = []  # i+1日目に働くのはL[i]日目以前

for i in range(N):
    if len(L) >= K:
        break
    if s[i] == 'o' and (L == [] or (i + 1) - L[-1] > C):
        # 出勤可能('o') 且 (Lが空又はi日目時点の最終出勤からc日経過)
        # ならばLにi+1を追加
        L.append(i + 1)

for i in range(N - 1, -1, -1):
    if len(R) >= K:
        break
    if s[i] == 'o' and (R == [] or R[-1] - (i + 1) > C):
        R.append(i + 1)

R.reverse()
ans = []

for i in range(K):
    if L[i] == R[i]:
        print(L[i])
