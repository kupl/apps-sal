# You lost the game.
n = int(input())
S = [str(input()) for _ in range(n)]
ok = -1
r = -1
for i in range(n):
    if S[i][0] == "O" and S[i][1] == "O":
        ok = 1
        r = i
        break
    elif S[i][3] == "O" and S[i][4] == "O":
        ok = 2
        r = i
        break
if r == -1:
    print("NO")
else:
    print("YES")
    for i in range(n):
        if r == i:
            if ok == 1:
                print("++|" + S[i][3] + S[i][4])
            else:
                print(S[i][0] + S[i][1] + "|++")
        else:
            print(S[i])
