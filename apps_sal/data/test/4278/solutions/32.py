from collections import Counter
n = int(input())
cnt_s = Counter([" ".join(sorted(input())) for i in range(n)])
print(sum(v*(v - 1)//2 for v in cnt_s.values()))
