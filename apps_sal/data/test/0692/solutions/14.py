n = int(input())
m = list(map(int, input().split()))
r = list(map(int, input().split()))

result = 0
for d in range(100000):
    for i in range(n):
        if d % m[i] == r[i]:
            result += 1
            break

print('%.6f' % (result / 100000))
