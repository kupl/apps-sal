# cook your dish here
n = int(input())


def compare(tpl):
    return tpl[1]


points = []
for i in range(n):
    a, b = map(int, input().split())
    points.append((a, b))
ans = 1
points.sort(key=compare)
end = points[0][1]
for a, b in points:
    if a > end:
        ans += 1
        end = b
print(ans)
