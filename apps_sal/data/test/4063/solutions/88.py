N = int(input())
ls = list(map(int, input().split(' ')))
ls.sort()
first_half = ls[:N // 2]
second_half = ls[N // 2:]
if first_half[-1] == second_half[0]:
    print(0)
else:
    print(second_half[0] - first_half[-1])
