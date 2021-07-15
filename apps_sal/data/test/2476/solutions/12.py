import bisect

n = int(input())
A = list(map(int, input().split()))
counts = [0]*(n)
for a in A:
    counts[a-1] += 1
counts.sort()

cumsum = []
num = 0
for count in counts:
    num += count
    cumsum.append(num)

answers = [0]*(n)
for i in range(1, n+1):
    idx = bisect.bisect_right(counts, i)
    left = cumsum[idx-1]
    right = (n-idx)*i
    K = (right+left)//i
    answers[K-1] = i

now = 0
for i in range(n-1, -1, -1):
    if answers[i] == 0:
        answers[i] = now
    now = answers[i]

for ans in answers:
    print(ans)
