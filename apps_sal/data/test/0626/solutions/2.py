n = int(input())

l = input().split()
l = [int(i) for i in l]

hacked = []

turns = -1

while len(hacked) < n:
    new = []
    for i in range(len(l)):
        if l[i] <= len(hacked):
            new = [i] + new
            hacked.append(i)
    for i in new:
        l.pop(i)
    l.reverse()
    turns += 1

print(turns)
