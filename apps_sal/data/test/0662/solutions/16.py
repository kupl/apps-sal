import sys
n = int(input())
for i in range(n):
    if i == 0:
        winner = 1
        looser = 2
        looker = 3
        a = int(input())
        if a == 3:
            print("NO")
            return
        if a == 1:
            looser, looker = looker, looser
        else:
            winner, looker = looker, winner
        continue
    a = int(input())
    if a == looker:
        print("NO")
        return
    if a == winner:
        looser, looker = looker, looser
    else:
        winner, looker = looker, winner
print("YES")
