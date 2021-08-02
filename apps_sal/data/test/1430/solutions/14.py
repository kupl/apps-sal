n, k = map(int, input().split())
s = input()
l = [["1", 0]]
for i in s:
    if l[-1][0] == i:
        l[-1][1] += 1
    else:
        l.append([i, 1])
if l[-1][0] == "0":
    l.append(["1", 0])
e = [0]
for i in range(len(l)):
    e.append(e[i] + l[i][1])
ans = 0 if k < len(l) // 2 else e[-1]
for i in range(2 * k - 1, len(l), 2):
    ans = max(ans, e[i + 2] - e[i - 2 * k + 1])
print(ans)
