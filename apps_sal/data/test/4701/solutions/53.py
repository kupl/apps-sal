N = int(input())
K = int(input())
ans = 1000
for i in range(N + 1):
    num = 1
    for s in range(i):
        num = num * 2

    for t in range(N - i):
        num += K

    if num < ans:
        ans = num

print(ans)
