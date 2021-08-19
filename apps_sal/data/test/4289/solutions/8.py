N = int(input())
(T, A) = map(int, input().split())
H = list(map(int, input().split()))
res = 0
for i in range(N):
    t1 = T - H[i] * 0.006
    t2 = T - H[res] * 0.006
    if abs(t1 - A) < abs(t2 - A):
        res = i
print(str(res + 1))
