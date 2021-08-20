(N, K) = list(map(int, input().split()))
pwds = [input() for _ in range(N)]
correct = input()
pwds = sorted([pwd for pwd in pwds if len(pwd) <= len(correct)], key=len)
time = 0
count = 0
i = 0
while len(pwds[i]) < len(correct):
    time += 1
    count += 1
    if count == K:
        time += 5
        count = 0
    i += 1
best = time + 1
while i < len(pwds) - 1:
    time += 1
    count += 1
    if count == K:
        time += 5
        count = 0
    i += 1
worst = time + 1
print(str(best) + ' ' + str(worst))
