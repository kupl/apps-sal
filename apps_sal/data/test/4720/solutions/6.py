n = int(input())
seat = [0] * (10 ** 5 + 1)
for i in range(n):
    l, r = list(map(int, input().split()))
    seat[l - 1] += 1
    seat[r] -= 1

for i in range(1, 10 ** 5):
    seat[i] += seat[i - 1]

res = 0
for i in range(10 ** 5):
    if seat[i] == 1:
        res += 1
print(res)
