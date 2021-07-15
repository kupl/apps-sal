from collections import Counter
n = int(input())
print("YES" if Counter(input().split()).most_common(1)[0][1] * 2 - 1 <= n else "NO")

