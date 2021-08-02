from collections import Counter
q = int(input())
for _ in range(q):
    n = int(input())
    s = list(map(int, input().split()))
    if n & 1:
        print("Second")
        continue
    flg = True
    c = Counter(s)
    for k, v in list(c.items()):
        if v % 2 == 1:
            flg = False
    print(("Second" if flg else "First"))
