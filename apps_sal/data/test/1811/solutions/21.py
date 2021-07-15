N, K = map(int,input().split())

obs = 0
cur = 0

S = input()

for s in S:
    if s == ".":
        cur = 0
    else:
        cur += 1
        obs = max(cur, obs)
        
if K <= obs:
    print("NO")
else:
    print("YES")
