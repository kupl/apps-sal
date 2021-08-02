Q = int(input())

queries = [list(map(int, input().split())) for _ in range(Q)]

max_num = 0
for _, r in queries:
    max_num = max(max_num, r)


is_prime = [True] * (max_num + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, max_num + 1):
    if not is_prime[i]:
        continue

    cnt = 2
    while i * cnt <= max_num:
        is_prime[i * cnt] = False
        cnt += 1

nums_like = [0] * (max_num + 1)
cnt = 0
for i in range(1, max_num + 1):
    if i % 2 == 0:
        nums_like[i] = nums_like[i - 1]
    else:
        if is_prime[i] and is_prime[(i + 1) // 2]:
            cnt += 1

        nums_like[i] = cnt


for l, r in queries:
    print((nums_like[r] - nums_like[l - 1]))
