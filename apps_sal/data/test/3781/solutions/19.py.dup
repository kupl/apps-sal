from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = Counter(map(int, input().split()))
    if n & 1:
        print("Second")
    else:
        win = False
        for k in a:
            if a[k] & 1:
                win = True
                break
        print("First" if win else "Second")
