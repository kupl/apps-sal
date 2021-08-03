from collections import Counter
w = input()
c = Counter(w)
ans = True
for v in c.values():
    if v % 2 == 1:
        ans = False
print("Yes" if ans == True else "No")
