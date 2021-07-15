k, p = list(map(int, input('').strip().split()))
answer = 0
before = 0
for i in range(k):
    if before == 0:
        before = 1
    else:
        before += 1
    now = int(str(before) + str(before)[::-1])
    answer = (answer + now) % p
print(answer)
