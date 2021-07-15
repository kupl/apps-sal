n = int(input())
str = input()
inp = list(map(int, input().split()))

for i in range(len(str)):
    if str[i] == '<':
        inp[i] *= -1

visited = [0 for i in range(n)]

cur = 0

while cur >= 0 and cur < n and visited[cur] != 1:
    visited[cur] = 1
    cur += inp[cur]

if cur >= 0 and cur < n:
    print("INFINITE")
else:
    print("FINITE")
