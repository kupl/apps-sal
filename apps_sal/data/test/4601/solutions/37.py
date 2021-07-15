N, K = list(map(int, input().split()))
hp_list = list(map(int, input().split()))

if N <= K:
    print(0)
else:
    hp_list.sort()
    del hp_list[N - K:N]
    print(sum(hp_list))
