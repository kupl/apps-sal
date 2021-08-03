n = int(input())
t, a = list(map(int, input().split()))
h = list(map(int, input().split()))

diff = []
for height in h:
    temp = t - (height * 0.006)
    diff.append(abs(a - temp))

minimum = min(diff)
ans = diff.index(minimum) + 1

print(ans)
