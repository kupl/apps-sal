n, c = list(map(int, input().split(" ")))
limak = 0
rade = 0
score = input().split(" ")
time = input().split(" ")
lTime = 0
rTime = 0
for i in range(n):
    lTime += int(time[i])
    limak += max(0, int(score[i]) - lTime * c)
    rTime += int(time[n - 1 - i])
    rade += max(0, int(score[n - 1 - i]) - rTime * c)
if limak > rade:
    print("Limak")
elif rade > limak:
    print("Radewoosh")
else:
    print("Tie")
