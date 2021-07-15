n, d = map(int, input().split())

current_max = 0
answer = 0

for i in range(d):
    s = list(str(input()))

    if s.count('1') != n:
        current_max += 1
    else:
        answer = max(current_max, answer)
        current_max = 0

answer = max(current_max, answer)
print(answer)
