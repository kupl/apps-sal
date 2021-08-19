import itertools
n = int(input())
a = list(map(int, input().split(" ")))
# print(a)
mini = 10 ** 10
suma = list(itertools.accumulate(a))
for i in range(0, n - 1):
    # print(suma[i],(suma[-1]))
    mini = min(mini, abs(suma[-1] - suma[i] * 2))
print(mini)
