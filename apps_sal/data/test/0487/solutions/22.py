n = int(input())
a = input().split()
e = 0
for i in range(n):
    e += int(a[i])
mini = ((2 * e) // n) + 1
for i in range(n):
    mini = max(int(a[i]), mini)
print(mini)
