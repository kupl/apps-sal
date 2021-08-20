N = int(input())
hard = 0
soft = 0
for _ in range(N):
    (_, tp) = input().split()
    if tp == 'hard':
        hard += 1
    else:
        soft += 1
top = max(soft, hard)
total = soft + hard
i = 1
while True:
    size = i * i
    val = size // 2
    if i % 2 != 0:
        val += 1
    if val >= top and size >= total:
        print(i)
        break
    i += 1
