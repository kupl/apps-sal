N, K = list(map(int, input().split()))
H = list(map(int, input().split()))
s = 0
for i in H:
    if i >= K:
        s = s + 1
print(s)
