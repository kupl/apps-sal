n = int(input())
a = list(map(int, input().split()))
a.sort()
contest = 1
for i in range(n):
    if a[i] >= contest:
        contest += 1
print(contest - 1)
