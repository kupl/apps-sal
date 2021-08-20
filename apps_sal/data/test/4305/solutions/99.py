(H, A) = list(map(int, input().split()))
k = 0
while H > 0:
    H -= A
    k += 1
print(k)
