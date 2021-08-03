n = int(input())
a = list(map(int, input().split()))
s = sorted(a)
q = a.index(max(a))
q1, q = min(len(a) - 1, q + 1), max(0, q - 1)
for q2 in range(len(a) - 2, -1, -1):
    if a[q] == s[q2]:
        q = max(0, q - 1)
    elif a[q1] == s[q2]:
        q1 = min(len(a) - 1, q1 + 1)
    else:
        print("NO")
        break
else:
    print("YES")
