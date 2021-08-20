(n, k, m) = map(int, input().split())
arr = [int(x) for x in input().split()]
k = min(k, m)
arr.sort()
s = [sum(arr)]
for i in range(1, len(arr)):
    s.append(s[i - 1] - arr[i - 1])
r = [0] * len(s)
for i in range(len(s)):
    f = m - i
    if f < 0:
        break
    r[i] = s[i] + min(k * (n - i), f)
    r[i] /= n - i
print(max(r))
