n = int(input())
a = [int(i) for i in input().split()]
if max(a) == 1:
    print("HARD")
else:
    print("EASY")
