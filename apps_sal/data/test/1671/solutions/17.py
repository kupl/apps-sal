n = int(input())
servers = list(map(int, input().split()))
s = sum(servers)
m = s // n
mod = s % n
total = 0
servers.sort()
for i in range(n - 1, n - mod - 1, - 1):
    total += abs(servers[i] - m - 1)
for i in range(n - mod - 1, -1, -1):
    total += abs(servers[i] - m)
print(total // 2)
