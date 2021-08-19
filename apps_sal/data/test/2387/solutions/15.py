import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())

S_p = []
S_n = []

for i in range(N):
    end = 0
    mim = 0
    for c in input():
        if c == "(":
            end += 1
        else:
            end -= 1
        mim = min(mim, end)

    if end >= 0:
        S_p.append([mim, end])
    else:
        S_n.append([end - mim, end])

S_p.sort(reverse=True)
S_n.sort(reverse=True)
# print(S_p)
# print(S_n)

check = 0
flag = True
for i in range(len(S_p)):
    if check + S_p[i][0] >= 0:
        check += S_p[i][1]
    else:
        flag = False
        break
    # print(check)

for i in range(len(S_n)):
    if check + S_n[i][1] - S_n[i][0] >= 0:
        check += S_n[i][1]
    else:
        flag = False
        break
    # print(check)

if check == 0 and flag:
    flag = True
else:
    flag = False

print("Yes" if flag else "No")
