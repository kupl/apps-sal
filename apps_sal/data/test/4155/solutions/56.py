a = int(input())
b = list(map(int, input().split()))
b.append(0)
ans = 0
while not max(b) == 0:
    for i in range(len(b)):
        if b[i] > 0 and b[i + 1] <= 0:
            ans += 1
    b = list([x - 1 for x in b])
print(ans)
