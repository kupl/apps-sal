n = int(input())
l = list(map(int, input().split()))
ans = []
yo = 0
count = 0
for i in range(n):
    ans.append([l[i], i + 1])
final = []
ans.sort(reverse=True)
for (a, b) in ans:
    count += yo * a + 1
    final.append(b)
    yo += 1
print(count)
print(*final)
