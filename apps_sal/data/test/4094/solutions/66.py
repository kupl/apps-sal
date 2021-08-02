
k = int(input())
r = 7 % k
for i in range(2 * k):
    if r == 0:
        print(i + 1)
        return
    r = (r * 10 + 7) % k
print(-1)
