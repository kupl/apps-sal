N = int(input())
V = list(map(int, input().split()))
odd_dict = {}
even_dict = {}
for i in range(N):
    if i % 2 == 0:
        if odd_dict.get(V[i]) is None:
            odd_dict[V[i]] = 1
        else:
            odd_dict[V[i]] += 1
    else:
        if even_dict.get(V[i]) is None:
            even_dict[V[i]] = 1
        else:
            even_dict[V[i]] += 1

odd_dict_sorted = sorted(list(odd_dict.items()), key=lambda a: a[1])
even_dict_sorted = sorted(list(even_dict.items()), key=lambda a: a[1])

odd_dict_max = odd_dict_sorted.pop()
even_dict_max = even_dict_sorted.pop()
if odd_dict_max[0] == even_dict_max[0] and N // 2 == odd_dict_max[1]:
    ans = N // 2
elif odd_dict_max[0] == even_dict_max[0]:
    odd_dict_max_t = odd_dict_sorted.pop()
    even_dict_max_t = even_dict_sorted.pop()
    ans = N - odd_dict_max[1] - max(even_dict_max_t[1],odd_dict_max_t[1])
else:
    ans = N - odd_dict_max[1] - even_dict_max[1]
print(ans)

