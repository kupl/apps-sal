b, k = list(map(int, input().split()))
r = 0
for i in map(int, input().split()):
    r = (b * r + i) % 2
print("odd" if r else "even")
