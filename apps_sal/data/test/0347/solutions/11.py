point = [500, 1000, 1500, 2000, 2500]
minutes = list(map(int, input().split()))
wrong = list(map(int, input().split()))
hack = list(map(int, input().split()))
answer = 0

for x, m, w in zip(point, minutes, wrong):
    answer += max(0.3 * x, (1 - m / 250) * x - 50 * w)

answer += hack[0] * 100 - hack[1] * 50

print(int(answer))
