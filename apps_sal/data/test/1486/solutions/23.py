n = int(input())
x = [int(i) for i in input().split()]

print(str(x[1] - x[0]) + " " + str(x[-1] - x[0]))

for i in range(n - 2):
    print(str(min(x[i + 1] - x[i], x[i + 2] - x[i + 1])) + " " + str(max(x[-1] - x[i + 1], x[i + 1] - x[0])))

print(str(x[-1] - x[-2]) + " " + str(x[-1] - x[0]))
