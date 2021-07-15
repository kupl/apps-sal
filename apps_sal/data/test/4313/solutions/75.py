n = int(input())
list_v = [int(i) for i in input().split()]
list_c = [int(j) for j in input().split()]
ans = 0
for i in range(0, n):
    if list_v[i] - list_c[i] > 0:
        ans += (list_v[i] - list_c[i])
print(ans)
