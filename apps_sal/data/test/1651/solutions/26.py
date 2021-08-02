S, P = map(int, input().split())
cnt = 0
for i in range(1, int(P**0.5) + 1):
    if P % i == 0:
        n = i
        m = P // i
        if n + m == S:
            cnt += 1
if cnt > 0:
    print("Yes")
else:
    print("No")
