n = int(input())
(a, b) = list(map(int, input().split()))
li = []
for i in range(n - 1):
    (x, y) = list(map(int, input().split()))
    li.append([x, y])
arr = [0] * (100 + 1)
for i in range(n - 1):
    arr[li[i][0]] += 1
    arr[li[i][1]] -= 1
(s, ans) = (0, 0)
for i in range(b + 1):
    if i > a and s == 0:
        ans += 1
    s += arr[i]
print(ans)
