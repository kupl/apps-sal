# B. DDoS
n = int(input())
r = [int(s) for s in input().split()]
ans = 0
for i in range(n, 0, -1):
    currsum = 0
    thresh = i*100
    for j in range(n):
        if j < i:
            currsum += r[j]
        else:
            currsum += r[j]
            currsum -= r[j-i]
        if currsum > thresh:
            ans = i
            break
    if ans > 0:
        break

print(ans)
