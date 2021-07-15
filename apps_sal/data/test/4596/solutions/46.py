n = int(input())
ls = list(map(int,input().split()))
ans = float("inf")
for i in range(n):
    p = 1
    while True:
        if ls[i] / (2 ** p) % 1 == 0:
            p += 1
        else:
            p -= 1
            break
    if p < ans:
        ans = p
print(ans)
