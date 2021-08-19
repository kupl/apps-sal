n = int(input())
h = list(map(int, input().split()))
ans = 0
for i in range(n):
    h_list = h[0:i + 1]
    highest = max(h_list)
    if highest <= h[i]:
        ans = ans + 1
print(ans)
