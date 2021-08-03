n = int(input())
L = list(map(int, input().split()))
s, f = list(map(int, input().split()))
count = 0
count_max = 0
ans = 0
for i in range(s - 1, f - 1):
    count += L[i]
for i in range(n):
    count -= L[f - 1]
    s -= 1
    f -= 1
    if s == -1:
        s = n - 1
    if f == -1:
        f = n - 1
    count += L[s]
    if count > count_max:
        count_max = count
        ans = i
print(ans + 1)
