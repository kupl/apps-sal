# ABC111

N = int(input())

zorome_contest = [111*i for i in range(1, 10)]
diff_min = 10**10
ans = 0

for contest in zorome_contest:
    if contest - N >= 0 and contest - N < diff_min:
        diff_min = contest - N
        ans = contest
print(ans)

