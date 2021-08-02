n = int(input())
a = list(map(int, input().split()))
prev = -1
ans = True
for i in range(n):
    if prev <= a[i] - 1:
        prev = a[i] - 1
    elif prev <= a[i]:
        continue
    else:
        ans = False

print("Yes" if ans == True else "No")
