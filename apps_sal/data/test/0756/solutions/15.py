n = int(input())
l = [0] + list(map(int, input().split())) + [900]
ans = 90
for i in range(1, n + 2):
    if l[i] - l[i - 1] > 15: ans = l[i - 1] + 15; break
print(min(90, ans))
