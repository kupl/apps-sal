import sys

S = []
A = set()
cnt = 0
r = 0
for i in range(2 * int(sys.stdin.readline().strip())):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == "add":
        S.append(int(cmd[1]))
    else:
        r += 1
        if S == []:
            if r in A:
                continue
        elif S[-1] == r:
            S.pop()
            continue
        else:
            cnt += 1
            A.union(S)
            S = []

print(cnt)
