from collections import Counter
n = int(input())
c = Counter(map(int, input().split()))
c_value = list(c.values())
overflow = sum(c_value) - len(c_value)
if overflow % 2 == 0:
    print(len(c_value))
else:
    print(len(c_value) - 1)
