(a, b, x, y) = map(int, input().split())
if b > a:
    route_x = x + 2 * x * (b - a)
    route_y = x + y * (b - a)
elif a == b:
    route_x = x
    route_y = x + y
else:
    route_x = x + 2 * x * (a - b - 1)
    route_y = x + y * (a - b - 1)
answer = min(route_x, route_y)
print(answer)
