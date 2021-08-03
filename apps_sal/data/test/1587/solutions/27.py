number = int(input())
date = input()
date = list(date)
cnt = 0
cnt2 = 0

for i in range(number):
    if date[i] == "R":
        cnt += 1

for s in range(cnt):
    if date[s] == "W":
        cnt2 += 1
print(cnt2)
