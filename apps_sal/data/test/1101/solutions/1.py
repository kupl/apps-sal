n, k = list(map(int, input().split()))
s = input()
prefixes = [0]
for i in range(n):
    prefixes.append(prefixes[i] + ((int(s[i])) + 1) % 2)
a = n
for i in range(n):
    if s[i] == '0':
        left = 0
        right = n
        while(right - left > 1):
            middle = (right + left) // 2
            if prefixes[min(n, 1 + i + middle)] - prefixes[max(0, i - middle)] > k:
                right = middle
            else:
                left = middle
        a = min(a, right)
print(a)
