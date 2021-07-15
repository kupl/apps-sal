n = int(input())
s = input().split()
sum = 0
for i in range(n):
    sum += int(s[i])
if sum > 0:
    print("HARD")
else:
    print("EASY")
