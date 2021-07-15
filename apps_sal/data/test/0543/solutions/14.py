k = int(input())
n = list(map(int, input().split()))
n.append(0)
res = True
for i in range(k + 1):
    if (n[i] < 0):
        res = False
        break
    if (n[i] % 2 == 0):
        continue
    elif (i < k):
        n[i+1] = n[i+1] - 1

if (res):
    print("YES")
else:
    print("NO")
