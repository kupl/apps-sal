x, y = map(int, input().split())
n = int(input())
z = y - x
var = [x, y, z, -x, -y, -z]
print(var[(n - 1) % 6] % 1000000007)
