N = int(input())
S = list(map(int, input().split()))

cnt = 1
min_n = S[0]
for n in S[1:]:
    if n <= min_n:
        min_n = n
        cnt += 1

print(cnt)
