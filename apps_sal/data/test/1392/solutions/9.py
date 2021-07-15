line = input()

integers = [int(i) for i in line.split()]
n = integers[0]
k = integers[1]

toTest = []
for i in range(n):
    line = input()
    toTest.append(line)

def test(num, n):
    arr = [0]*(10)
    goal = [1]*(n+1)
    for i in range(10, n+1, -1):
        goal.append(0)
    for i in range(len(num)):
        if goal[int(num[i])] == 1:
            arr[int(num[i])] = 1
    if arr == goal:
        return 1
    else:
        return 0

total = 0
for num in toTest:
    total += test(num, k)

print(total)

