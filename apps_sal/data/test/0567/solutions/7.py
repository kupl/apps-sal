n = int(input())
pr = [int(x) for x in input().split()]
sec = 0
for elem in pr:
    you = elem - 1
    fri = 10 ** 6 - elem
    sec = max(sec, min(you, fri))
print(sec)
