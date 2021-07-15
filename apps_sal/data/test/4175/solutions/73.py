n = int(input())
w = list(input() for _ in range(n))
ans = True
w2 = set(w)
if len(w) != len(w2):
    ans = False
for i in range(n-1):
    if w[i][-1] != w[i+1][0]:
        ans = False
if ans:
    print("Yes")
else:
    print("No")
