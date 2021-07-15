n = int(input())
l = list(map(int, input().split()))
b = 10 ** 9
for i in range(0, len(l)):
    b = min(b, l[i] / max(i, n - i - 1))
print(int(b))
