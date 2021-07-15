n = int(input())
s = input()
if n > 26:
    print(-1)
else:
    A = set()
    for i in range(n):
        A.add(s[i])
    print(n - len(A))
