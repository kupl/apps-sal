(A, B, K) = map(int, input().split())
common_list = []
min_AB = min(A, B)
for i in range(1, min_AB + 1):
    if A % i == 0 and B % i == 0:
        common_list.append(i)
common_list.sort(reverse=True)
print(common_list[K - 1])
