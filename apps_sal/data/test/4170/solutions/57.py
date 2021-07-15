n = int(input())
h = list(map(int, input().split()))
l = [-1]
for i in range(n-1):
    if h[i] < h[i+1]:
        l.append(i)
    elif i == n-2:
        l.append(n-1)
ans = 0
for j in range(len(l)-1):
    num = l[j+1] - l[j] - 1
    ans = max(num, ans)
print(ans)
