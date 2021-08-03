S = input()

# 0を基準として、0と1の境目を調べる
boundary = []
pre_state = '0'
for i in range(len(S)):
    if S[i] != pre_state:
        boundary.append(i)
        pre_state = S[i]
else:
    if S[-1] == '1':
        boundary.append(len(S))

if len(boundary) == 0:
    print((len(S)))
    return

# 答えは、端から一番遠い境目
lst = []
for i in range(len(boundary)):
    lst.append(max(boundary[i], len(S) - boundary[i]))
ans = min(lst)
print(ans)
