(k, n) = list(map(int, input().split()))
a = list(map(int, input().split()))
a1 = sorted(a)
temp = list()
x = len(a) - 1
for i in range(x):
    temp.append(a1[i + 1] - a1[i])
temp.append(min(max(a) - min(a), k - max(a) + min(a)))
ans = k - max(temp)
print(ans)
