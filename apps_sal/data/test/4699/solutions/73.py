from itertools import count
(n, k) = map(int, input().split())
D = set(map(int, input().split()))
for ans in count(n, 1):
    for c in str(ans):
        if int(c) in D:
            break
    else:
        print(ans)
        break
