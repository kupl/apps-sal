from collections import Counter
n = int(input())
print("First" if any(i & 1 for i in map(int, input().split())) else "Second")
