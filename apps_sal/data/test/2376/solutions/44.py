# solution
import io

nim, mike = [int(_) for _ in input().split()]
WV = [[int(_) for _ in input().split()] for _ in range(nim)]
qwe = {}
qwe[0] = 0
for weight, value in WV:
    dp_old = qwe.copy()
    for k, v in list(dp_old.items()):
        if k + weight <= mike:
            qwe[k + weight] = max(qwe.get(k + weight, 0), v + value)
ans = 0
for k, v in list(qwe.items()):
    ans = max(ans, v)
print(ans)

