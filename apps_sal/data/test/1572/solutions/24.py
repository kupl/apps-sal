a = int(input())
if a == 1:
    print(1)
    quit()
x = list(map(int, input().split(' ')))
new = [0] * a
for i in range(2, a):
    if x[i] == x[i - 1] + x[i - 2]:
        new[i] = 1

streak = 0
maxstr = 2
for i in new:
    if i == 1:
        streak += 1
    else:

        maxstr = max(streak + 2, maxstr)
        streak = 0
maxstr = max(streak + 2, maxstr)
print(maxstr)
