(n, m) = map(int, input().split())
hosts = [0]
hosts += list(map(int, input().split()))
for i in range(1, n + 1):
    hosts[i] += hosts[i - 1]
letters = list(map(int, input().split()))
j = 0
for i in range(m):
    while hosts[j] < letters[i]:
        j += 1
    print(j, letters[i] - hosts[j - 1])
