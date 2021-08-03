N, M, X, Y = [int(i) for i in input().split()]
x_list = [int(i) for i in input().split()]
y_list = [int(i) for i in input().split()]

x_max = max(x_list)
y_min = min(y_list)

ans = "War"
for Z in range(X + 1, Y + 1):

    if x_max < Z <= y_min:
        ans = "No War"
        break

print(ans)
