N = int(input())
A = list(map(int, input().split()))
s = set(A)

if len(s) % 2 == 0:
    ans = len(s) - 1
else:
    ans = len(s)
print(ans)
