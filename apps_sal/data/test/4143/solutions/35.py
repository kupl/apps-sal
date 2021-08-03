n = int(input())
t = [int(input()) for i in range(5)]
k = 0
for i in range(5):
    k = max(k, (n + t[i] - 1) // t[i])
print(k + 4)
