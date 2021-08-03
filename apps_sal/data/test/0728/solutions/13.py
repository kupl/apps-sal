N = int(input())
votes = [int(x) for i, x in enumerate(input().split())]
my = votes[0]
old = my
votes = sorted(votes[1:], key=lambda x: -x)
while my <= votes[0]:
    votes[0] -= 1
    my += 1
    i = 0
    while i + 1 < len(votes) and votes[i] < votes[i + 1]:
        votes[i], votes[i + 1] = votes[i + 1], votes[i]
        i += 1
print(my - old)
