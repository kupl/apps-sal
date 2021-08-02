N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

add = sorted([x + y for x, y in xy])
sub = sorted([x - y for x, y in xy])

print(max(add[-1] - add[0], sub[-1] - sub[0]))
