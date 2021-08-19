(k, x) = map(int, input().split())
ans = [i for i in range(abs(x) - k + 1, abs(x) + k)]
for i in ans:
    if -1000000 <= i <= 1000000:
        print(i, '', end='')
