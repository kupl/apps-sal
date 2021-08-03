a, b = list(map(int, input().split()))
n = [0] * b
for i in range(a):
    k = int(input())
    n[k - 1] += 1
cnt = 0
for x in n:
    cnt += x % 2
print(a - cnt // 2)
