import sys
input = sys.stdin.readline
for j in range(int(input())):
    a, b, p = list(map(int, input().split(" ")))
    s = input().rstrip()

    costs = [0 for x in range(len(s))]

    costs[len(s) - 1] = 0
    if(s[len(s) - 2] == "B"):
        costs[len(s) - 2] = b
    else:
        costs[len(s) - 2] = a
    for it in range(3, len(s) + 1):
        if(s[len(s) - it] != s[len(s) - it + 1]):
            costs[len(s) - it] = costs[len(s) - it + 1] + (s[len(s) - it] == "A") * a + (s[len(s) - it] == "B") * b
        else:
            costs[len(s) - it] = costs[len(s) - it + 1]

    for j in range(len(costs)):
        if(costs[j] <= p):
            print(j + 1)
            break
