n = int(input())
m = list(map(int, input().split()))
starts = sorted([(i - m[i], i) for i in range(n)], reverse = True)
cur = answer = 0
for i in range(n):
    while starts[-1][1] < i:
        starts.pop()
    cur = max(cur, i - starts[-1][0])
    answer += cur - m[i]
print(answer)

