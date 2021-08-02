n = int(input())
line = input().split()

lst = []
for num in line:
    lst.append(int(num))

ans = lst[1] - lst[0]
mn = lst[2] - lst[0]
for i in range(2, n):
    ans = max(ans, lst[i] - lst[i - 1])
    mn = min(mn, lst[i] - lst[i - 2])

ans = max(ans, mn)
print(str(ans))
