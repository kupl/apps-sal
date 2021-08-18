display = sorted(list(map(int, input().split())))
K = int(input())

maximum = display[-1]
for i in range(K):
    maximum = maximum * 2
print(sum(display[:-1]) + maximum)
