(n, i) = list(map(int, input().split()))
k = 2 ** (8 * i // n) if 8 * i // n < 20 else n
a = [int(x) for x in input().split()]
a.sort()
freq = [1]
for i in range(1, len(a)):
    if a[i - 1] == a[i]:
        freq[-1] += 1
    else:
        freq.append(1)
window = sum(freq[:k])
ans = window
for i in range(k, len(freq)):
    window += freq[i]
    window -= freq[i - k]
    ans = max(ans, window)
print(n - ans)
