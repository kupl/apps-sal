N, A, B = list(map(int, input().split()))
res = 0

for i in range(1, N + 1):
    num = sum(map(int, list(str(i))))
    if A <= num <= B:
        res += i

print(res)
