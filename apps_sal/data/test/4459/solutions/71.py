N = int(input())
lst = list(map(int, input().split()))
lst.sort()
freq = {}
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
ans = 0
for (key, value) in freq.items():
    if key > value:
        ans += value
    elif key < value:
        ans += abs(key - value)
print(ans)
