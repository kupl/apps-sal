x, y, z, k = map(int, input().split())
alst = list(map(int, input().split()))
blst = list(map(int, input().split()))
clst = list(map(int, input().split()))
alst.sort(reverse=True)
blst.sort(reverse=True)
clst.sort(reverse=True)
ans = []
for i in range(x):
    for j in range(y):
        if i * j > k:
            break
        for l in range(z):
            if i * j * l > k:
                break
            ans.append(alst[i] + blst[j] + clst[l])
ans.sort(reverse=True)
print(*ans[:k], sep="\n")
