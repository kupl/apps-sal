n = int(input())
hito = 0
for i in range(n):
    l, r = map(int, input().split())
    hito += r - l + 1
print(hito)
