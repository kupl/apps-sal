details = list(map(int, input().split()))
N = details[0]
M = details[1]
first = []
second = []
for i in range(M):
    det = list(map(int, input().split()))
    first.append(det[0])
    second.append(det[1])
maxi = max(first)
mini = min(second)
if mini - maxi >= 0:
    print(mini - maxi + 1)
else:
    print(0)
