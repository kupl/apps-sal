(n, l) = map(int, input().split())
l_list = [l + i - 1 for i in range(1, n + 1)]
ab_list = [abs(i) for i in l_list]
num = ab_list.index(min(ab_list))
print(sum(l_list) - l_list[num])
