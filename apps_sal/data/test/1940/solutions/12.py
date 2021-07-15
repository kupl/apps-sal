n, k = map(int, input().split())
days = 0
w = list(map(int, input().split()))
for wi in w:
    days += (wi - 1) // k + 1
print((days - 1) // 2 + 1)
