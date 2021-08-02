n = int(input())
ln = sorted(list(map(int, input().split())) for _ in range(n))
m = int(input())
lm = sorted(list(map(int, input().split())) for _ in range(m))
lln = sorted(x[::-1] for x in ln)
llm = sorted(x[::-1] for x in lm)
ans = ln[-1][0] - llm[0][0]
if lm[-1][0] - lln[0][0] > ans: ans = lm[-1][0] - lln[0][0]
print(max(0, ans))
