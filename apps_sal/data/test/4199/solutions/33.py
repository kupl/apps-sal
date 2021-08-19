(N, K) = list(map(int, input().split()))
H = list(map(int, input().split()))
s = 0
for i in H:
    if K <= i:
        s += 1
print(s)
