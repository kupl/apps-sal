n = int(input())
(t, a) = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
diff = 100000
for (i, ele) in enumerate(arr):
    temp = t - ele * 0.006
    if abs(a - temp) < diff:
        diff = abs(a - temp)
        ans = i + 1
print(ans)
