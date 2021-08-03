n = int(input())
ip = list(map(int, input().split()))
ip2 = []
for i in range(n):
    ip2.append((i, ip[i]))
ip2 = sorted(ip2, key=lambda x: x[1])
for i in range(n // 2):
    print(ip2[i][0] + 1, ip2[n - i - 1][0] + 1)
