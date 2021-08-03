n = int(input())
ans = []

for i in range(n + 1):
    cnt = 0
    if i % 2:
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt == 8:
            ans.append(i)

print((len(ans)))
