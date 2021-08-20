(N, L) = map(int, input().split())
tastes = []
for i in range(1, N + 1):
    tastes.append(L + i - 1)
abs_tastes = list(map(abs, tastes))
min_tastes_index = abs_tastes.index(min(abs_tastes))
tastes.pop(min_tastes_index)
print(sum(tastes))
