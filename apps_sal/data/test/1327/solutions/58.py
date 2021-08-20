import copy
(n, m) = list(map(int, input().split()))
temp = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for x_sign in (1, -1):
    for y_sign in (1, -1):
        for z_sign in (1, -1):
            params = copy.deepcopy(temp)
            for xyz in params:
                xyz.append(x_sign * xyz[0] + y_sign * xyz[1] + z_sign * xyz[2])
            params.sort(key=lambda xyz: xyz[3], reverse=True)
            ans_sign = sum([xyz[3] for xyz in params[:m]])
            ans = max(ans, ans_sign)
print(ans)
