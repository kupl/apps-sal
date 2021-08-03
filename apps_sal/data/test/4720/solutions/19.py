n = int(input())
kei = 0
for i in range(n):
    l, r = map(int, input().split())
    kei += r - l + 1
print(kei)
