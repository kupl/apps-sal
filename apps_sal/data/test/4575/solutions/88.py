n = int(input())
d, x = (int(i) for i in input().split())
list_a = [int(input()) for i in range(0, n)]
ans = x
for i in list_a:
    for j in range(1, d + 1):
        if i == 1:
            ans += d
            break
        elif j % i == 1:
            ans += 1
print(ans)
