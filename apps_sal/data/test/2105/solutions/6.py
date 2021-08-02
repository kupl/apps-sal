n, m = list(map(int, input().split()))
s = list(input().split())
t = list(input().split())
for _ in range(int(input())):
    y = int(input())
    print(s[(y - 1) % n] + t[(y - 1) % m])
