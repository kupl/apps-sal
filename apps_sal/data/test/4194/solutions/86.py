(N, M) = list(map(int, input().split()))
work = list(map(int, input().split()))
if N >= sum(work):
    answer = N - sum(work)
else:
    answer = '-1'
print(answer)
