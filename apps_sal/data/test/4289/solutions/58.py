N = int(input())
(T, A) = map(int, input().split())
S = 1000000
l = [int(x) for x in input().split()]
for i in range(len(l)):
    s = abs(T - l[i] * 0.006 - A)
    if s < S:
        S = s
        ans = i
print(ans + 1)
