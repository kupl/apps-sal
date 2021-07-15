n, k = [int(z) for z in input().split()]
ans = [0] * 16
for i in range(n):
    problem = [int(z) for z in input().split()]
    s = 0
    for j in range(k):
        s = s * 2 + problem[j]
    ans[s] += 1
#print(ans)
for i in range(16):
    for j in range(16):
        if ans[i] > 0 and ans[j] > 0 and (i & j) == 0:
            print("YES")
            return
print("NO")
