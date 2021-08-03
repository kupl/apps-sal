n, x = list(map(int, input().split()))
c = list(map(int, input().split()))

c.sort()
res = 0
learn_time = x
for i in range(n):
    res += c[i] * learn_time
    if learn_time > 1:
        learn_time -= 1
print(res)
