N = int(input())
(T, A) = map(int, input().split())
H = list(map(int, input().split()))
h_c = (T - A) * 1000 / 6
res = 10 ** 5
ind = 0
for i in range(N):
    if res > abs(H[i] - h_c):
        ind = i + 1
        res = abs(H[i] - h_c)
print(ind)
