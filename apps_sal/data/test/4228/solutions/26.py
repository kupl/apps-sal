n, l = list(map(int, input().split()))
apple_list = [l + i for i in range(n)]
abs_min = min([abs(apple) for apple in apple_list])
apple_list.remove(abs_min if abs_min in apple_list else -abs_min)
print((sum(apple_list)))

