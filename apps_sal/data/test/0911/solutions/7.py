nc = list(map(int, input().split()))
n = nc[0]
c = nc[1]
points = list(map(int, input().split()))
times = list(map(int, input().split()))
lPoints = 0
rPoints = 0
# split into two, test l and r separately
timeSpent = 0
for i in range(n):
    timeSpent += times[i]
    lPoints += max(0, (points[i] - (timeSpent * c)))
# do Radewoosh
timeSpent = 0
i = n - 1
while i >= 0:
    timeSpent += times[i]
    rPoints += max(0, (points[i] - (timeSpent * c)))
    i -= 1
if rPoints > lPoints:
    print("Radewoosh")
elif lPoints > rPoints:
    print("Limak")
else:
    print("Tie")
