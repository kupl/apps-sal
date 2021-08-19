N = int(input())
seat = 0
for i in range(N):
    (l, r) = map(int, input().split())
    seat += r - l + 1
print(seat)
