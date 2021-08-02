n = int(input())
lst = [int(x) for x in input().split()]

power = 0
answer = 0
while power != len(lst):
    for i in range(len(lst)):
        if lst[i] <= power:
            power += 1
            lst[i] = float('inf')

    if power == len(lst):
        break
    answer += 1

    for i in range(len(lst) - 1, -1, -1):
        if lst[i] <= power:
            power += 1
            lst[i] = float('inf')

    if power == len(lst):
        break
    answer += 1

print(answer)
