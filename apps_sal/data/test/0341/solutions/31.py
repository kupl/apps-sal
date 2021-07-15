from collections import deque
n,k = map(int, input().split())
r,s,p = map(int, input().split())

point = {}
point["r"]=r
point["s"]=s
point["p"]=p

t = input()
# グー:r
# チョキ:s
# パー:p

def janken(opp, rireki, point, k):
    if opp=="r":
        rireki.append("p")
        return point["p"]
    elif opp=="s":
        rireki.append("r")
        return point["r"]
    elif opp=="p":
        rireki.append("s")
        return point["s"]
    
        
ans = 0
rireki = deque()
for i in range(n):
    hand = t[i]
    ans += janken(hand, rireki, point, k)
for i in range(k,n):
    if rireki[i]==rireki[i-k]:
        ans -= point[rireki[i]]
        rireki[i]="else"
print(ans)
