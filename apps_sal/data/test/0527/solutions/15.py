# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
S = input().rstrip()
T = input().rstrip()

# set:T が set:S に含まれない => S にない文字を T で使っていたら
if not set(T) <= set(S):
    print((-1))
    return

ind = -1
cnt = 0
for t in T:
    # 現在の index 以降から探索する
    ind = S.find(t,ind+1)
    # 見つからない場合は先頭から探索し直し, loop countを+1
    if ind == -1:
        cnt += 1
        ind = S.find(t)

print((len(S) * cnt + ind + 1))

