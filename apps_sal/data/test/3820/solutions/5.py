n, m = list(map(int, input().split()))
s = input()
t = input()
k = s.find("*")
if k == -1 or n > m + 1:
    if s == t:
        print("YES")
    else:
        print("NO")
else:
    if s[:k] == t[:k] and s[k+1:] == t[m - (n - k - 1):]:
        print("YES")
    else:
        print("NO")

