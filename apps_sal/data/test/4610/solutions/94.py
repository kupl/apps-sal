(N, K) = map(int, input().split())
a_list = list(map(int, input().split()))
counter_list = [0] * N
for i in a_list:
    counter_list[i - 1] += 1
counter_list.sort(reverse=True)
ans = N - sum(counter_list[:K])
print(ans)
