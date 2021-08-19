n = int(input())
t = [False] * 2521
sum = 0
for a in range(2521):
    t[a] = a % 2 == 0 or a % 3 == 0 or a % 4 == 0 or (a % 5 == 0) or (a % 6 == 0) or (a % 7 == 0) or (a % 8 == 0) or (a % 9 == 0) or (a % 10 == 0)
    if not t[a]:
        sum += 1
ret = sum * (n // 2520)
for a in range(n % 2520 + 1):
    ret += not t[a]
print(ret)
