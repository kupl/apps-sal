import sys
input = sys.stdin.readline
n = int(input())
num_edge = 0
num_vertex = 0
for i in range(1, n):
    u_v = list(map(int, input().split()))
    u = u_v[0]
    v = u_v[1]
    if v < u:
        tmp = v
        v = u
        u = tmp
    num_edge += u * (n - v + 1)
    num_vertex += i * (n - i + 1)
num_vertex += n
print(num_vertex - num_edge)
