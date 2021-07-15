from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 1:
        print("Second")
    elif all(i % 2 == 0 for i in Counter(a).values()):
        print("Second")
    else:
        print("First")
