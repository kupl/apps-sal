(N, K) = map(int, input().split())
a = list(map(int, input().split()))
a_dict = {}
for i in range(N):
    if a[i] not in a_dict.keys():
        a_dict[a[i]] = 1
    else:
        a_dict[a[i]] += 1
ans = 0
if len(a_dict) <= K:
    print(ans)
else:
    sort_a_dict_list = sorted(a_dict.items(), key=lambda x: x[1])
    for j in range(len(a_dict) - K):
        ans += sort_a_dict_list[j][1]
    print(ans)
