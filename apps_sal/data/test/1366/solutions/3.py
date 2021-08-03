n = int(input())
a = [0] * n
b = [0] * n
ans = 0
for i in range(n):
    a[i], b[i] = map(int, input().split())
for i in range(n):
    for j in range(n):
        if i != j and b[j] == a[i]:
            break
    else:
        ans += 1
print(ans)
