print(sum(((lambda x: x[0] + 2 <= x[1])(list(map(int, input().split()))) for x in range(int(input())))))
