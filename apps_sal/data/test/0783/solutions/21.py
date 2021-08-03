n = int(input())
li = list(map(int, input().split(" ")))
lu = []
k = 0
for i in range(n - 1, -1, -1):
    lu.append(max(0, k + 1 - li[i]))
    k = max(k, li[i])
lu.reverse()
print(' '.join(map(str, lu)))
