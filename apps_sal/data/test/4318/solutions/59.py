n = int(input())
h = list(map(int, input().split()))
h_list = [h[0]]
ans = 1
for i in range(1, n):
    h_list.append(h[i])
    if h[i] >= max(h_list):
        ans += 1
print(ans)
