n, m = map(int, input().split())
li = [0]*200001
s = "IMPOSSIBLE"
for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        if li[b] == 0:
            li[b] = 1
        else:
            s = "POSSIBLE"
    
    if b == n:
        if li[a] == 0:
            li[a] = 1
        else:
            s = "POSSIBLE"

print(s)
