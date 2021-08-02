n = int(input())
s = 0
l = list(map(int, input().split()))
for i in l:
    s += i
if ((n * (n + 1)) / 2) == s:
    print("YES")
else:
    print("NO")
