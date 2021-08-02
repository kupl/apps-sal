##初期値設定##
N, Q = map(int, input().split())
S = input()
dl = []
dr = []
for i in range(Q):
    line = list(map(int, input().split()))
    dl.append(line[0])
    dr.append(line[1])

##ACの個数配列計算##
a = []
for i in range(N - 1):
    tmp_S = S[i:i + 2]
    if tmp_S == "AC":
        a.append(1)
    else:
        a.append(0)

##累積和計算##
s = [0]
for i in range(len(a)):
    s.append(s[i] + a[i])

##解答算出##
ans = []
for l, r in zip(dl, dr):
    ans.append(s[r - 1] - s[l - 1])

for i in range(Q):
    print(ans[i])
