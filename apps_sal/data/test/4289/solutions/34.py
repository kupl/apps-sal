N = int(input())
(T, A) = map(int, input().split())
H = list(map(int, input().split()))
cnt = []
for h in H:
    a = T - h * 0.006
    c = abs(A - a)
    cnt.append(c)
ans = cnt.index(min(cnt)) + 1
print(ans)
