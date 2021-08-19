input()
l = list(map(int, input().split()))
ans = 0
l2 = [0] * int(200000.0 + 5)
for i in range(len(l)):
    l2[l[i]] = i + 1
for i in range(1, len(l)):
    ans += abs(l2[i] - l2[i + 1])
print(ans)
