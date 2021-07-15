n = int(input())
ab = []
for _ in range(n):
    ab.append(tuple(map(int,input().split())))

ab = sorted(ab,key=lambda x:x[1])
ans = True
t = 0
for i in range(n):
    t += ab[i][0]
    if t>ab[i][1]:
        ans = False
print("Yes" if ans==True else "No")
