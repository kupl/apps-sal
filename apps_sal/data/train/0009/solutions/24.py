import math
test = int(input())
for t in range(test):
    s = input()
    n = len(s)
    A = []
    o = 0
    for i in range(n):
        if s[i] == '1':
            o += 1
        else:
            A.append(o)
            o = 0
    if s[n - 1] == '1':
        A.append(o)
    A.sort(reverse=True)
    ans = 0
    for i in range(0, len(A), 2):
        ans += A[i]
    print(ans)
