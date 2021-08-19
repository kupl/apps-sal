(n, k) = list(map(int, input().split()))
s = input()
sorted_chars = sorted(set(s))
inv_mapping = {a: i for (i, a) in enumerate(sorted_chars)}
if k <= n:
    i = k - 1
    while s[i] == sorted_chars[-1] and i >= 0:
        i -= 1
    if i >= 0:
        print(s[:i] + sorted_chars[inv_mapping[s[i]] + 1] + (k - i - 1) * sorted_chars[0])
    else:
        print(sorted_chars[inv_mapping[s[0]] + 1] + (k - 1) * sorted_chars[0])
else:
    print(s + (k - n) * sorted_chars[0])
