N = int(input())

sm = 0

for i in range(N):
    l, r = map(int, input().split())
    sm += r - l + 1

print(sm)
