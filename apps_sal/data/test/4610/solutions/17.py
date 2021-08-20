(n, k) = map(int, input().split())
l = list(map(int, input().split()))
freq = [0] * (n + 1)
for i in l:
    freq[i] += 1
freq.sort()
print(sum(freq[:n - k + 1]))
