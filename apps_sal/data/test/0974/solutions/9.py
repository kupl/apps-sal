n = int(input())
mas = []
current = 1
count = 0

for i in range(2 * n):
    instruct = input().split()
    if instruct[0] == 'add':
        mas.append(int(instruct[1]))
    else:
        if len(mas) > 0:
            if mas[-1] == current:
                mas.pop()
            else:
                mas = []
                count += 1

        current += 1
print(count)

