N = int(input())
a = [int(input()) - 1 for _ in range(N)]
x = 0
ans = 0
while True:
    ans += 1
    x = a[x]
    if x == 1:
        print(ans)
        break
    if ans > N:
        print((-1))
        break;
