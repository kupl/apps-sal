n = int(input())
subject = list(map(int, input().split()))
pupils = [[], [], []]
for i in range(n):
    pupils[subject[i] - 1].append(i + 1)
print(min(len(pupils[0]), len(pupils[1]), len(pupils[2])))
for i in range(min(len(pupils[0]), len(pupils[1]), len(pupils[2]))):
    print(pupils[0][i], pupils[1][i], pupils[2][i])
