import collections
n = int(input())
a = list(map(int, input().split()))
lower_a = list(map(lambda x: x - 1, a))
upper_a = list(map(lambda x: x + 1, a))
extended_a = collections.Counter(a + lower_a + upper_a)
print(extended_a.most_common()[0][1])
