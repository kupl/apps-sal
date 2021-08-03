n = int(input())
p = list(map(int, input().split()))
p.sort(reverse=True)
# 追加していく際に追加した数の両脇を固める
s = 0
for i in range(1, n):
    s += p[i // 2]

print(s)
