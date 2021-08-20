n = int(input())
masses = input().split()
muscle = ['chest', 'biceps', 'back']
i = 0
res = [0] * 3
for mass in masses:
    res[i % 3] += int(mass)
    i += 1
print(muscle[res.index(max(res))])
