e1, e2 = map(str, input().split())
c = []
count = 0
ans = 0
for i in range(int(e1), int(e2) + 1):
    count = 0
    for k in range(len(str(i)) // 2):
        if str(i)[k] == str(i)[-(k + 1)]:
            count += 1
            if len(str(i)) // 2 == count:
                ans += 1

print(ans)
