n = int(input())

lst = [int(x) for x in input().split()]

if sum(lst) > 0:
    print("HARD")
else:
    print("EASY")

