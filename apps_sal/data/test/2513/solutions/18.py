# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------

def check(a0, a1):
    b0,b1 = a0,a1
    Ans = a1
    for i in range(N):
        # 羊
        if a1 == "S":
            # 両隣が同じ
            if S[i] == "o":
                a2 = a0
            else:
                a2 = B[a0]
        # 狼
        else:
            # 両隣が異なる
            if S[i] == "o":
                a2 = B[a0]
            else:
                a2 = a0
        Ans += a2
        a0,a1 = a1,a2
    if Ans[0] == Ans[N] and Ans[0] == b1 and Ans[N-1] == b0:
        return Ans[0:N]
    else:
        return -1

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
S = input().rstrip()

B = {"S":"W", "W":"S"}
S0S1 = [("S","S"), ("S","W"), ("W","S"), ("W","W")]

for s0,s1 in S0S1:
    Ans = check(s0,s1)
    if Ans != -1:
        print(Ans)
        return

print((-1))


