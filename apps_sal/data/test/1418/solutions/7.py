n = int(input())


ans = [0]*(n+1)
count = 1
for i in range(2, n+1):
    if ans[i] == 0:
        for j in range(i, n+1, i):
            ans[j] = count
        count += 1

print(" ".join(map(str, ans[2:])))

