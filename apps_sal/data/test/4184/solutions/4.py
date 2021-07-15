n = int(input())
w = list(map(int, input().split()))
wmax = 9999999999
for i in range(1, n):
    if wmax >= abs(sum(w[i:]) - sum(w[:i])):
        wmax = abs(sum(w[i:]) - sum(w[:i]))
print(wmax)
