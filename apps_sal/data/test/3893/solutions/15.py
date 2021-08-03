x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
n = int(input())
r = 0
for i in range(n):
    q = list(map(int, input().split()))
    r = r + ((q[0] * x1 + q[1] * y1 + q[2]) * (q[0] * x2 + q[1] * y2 + q[2]) < 0)
print(r)
