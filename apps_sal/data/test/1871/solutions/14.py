n, x = list(map(int, input().split(' ')))
cs = list(map(int, input().split(' ')))

x_work = list(range(x, 0, -1)) + [1] * n
cs.sort()


answer = 0
for i, item in enumerate(cs):
    answer += x_work[i] * item

print(answer)
