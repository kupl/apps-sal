n = int(input())
a = sorted(list(map(int, input().split())))

ans = 0
for i in a:
    if i % 2 == 0:
        while i % 2 == 0:
            ans += 1
            i //= 2
print(ans)
