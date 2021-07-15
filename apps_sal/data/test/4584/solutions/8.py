n = int(input())
a = list(map(int, input().split()))
a.append(0)
a.sort()

flg = [0 for i in range(n)]
for i in range(n):
    flg[a[i]] += 1
for i in range(n-1):
    print(flg[i+1])

print(0)
