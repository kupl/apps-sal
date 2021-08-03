n = int(input())
li = list(map(int, input().split()))

li = sorted(zip(li, list(range(len(li)))))[::-1]
ans = 0

for i in range(n):
    ans += li[i][0] * i + 1
print(ans)
ans_li = []
for i in range(n):
    ans_li.append(li[i][1] + 1)
print(*ans_li)
