n = int(input())
a = list(map(int, input().split()))
last = -1
ans = 1
for i in range(n):
    if a[i] == 1:
        if last != -1:
            ans *= i - last
        last = i

print(ans if last != -1 else 0)

