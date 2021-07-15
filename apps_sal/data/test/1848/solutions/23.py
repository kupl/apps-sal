from collections import Counter
n = int(input())
print(n - Counter(list(map(int, input().split()))).most_common(1)[0][1])

