n = int(input())
a = list(map(int, input().split()))
mx = max(a)
mn = min(a)
for i in range(len(a)):
    if a[i] == mn:
        i_min = i
    if a[i] == mx:
        i_max = i
print(max(i_max, i_min, len(a) - i_max - 1, len(a) - i_min - 1))
