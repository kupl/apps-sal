a = int(input())
a = list(map(int, input().split()))
b = int(input())
b = list(map(int, input().split()))
a = sorted(a)
b = reversed(sorted(b))
x = [0] * 200
for t in a:
    x[t] += 1

ans = 0
for t in b:
    if x[t + 1]:
        ans += 1
        x[t + 1] -= 1
        continue
    if x[t]:
        ans += 1
        x[t] -= 1
        continue
    if x[t - 1]:
        ans += 1
        x[t - 1] -= 1
        continue

print(ans)
