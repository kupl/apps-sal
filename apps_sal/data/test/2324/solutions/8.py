s = input()
n = len(s)
max_palin = [[0 for i in range(n + 1)] for j in range(n + 1)]
count = [0 for i in range(n + 1)]
for sub_len in range(1, n + 1):
    for left in range(0, n - sub_len + 1):
        right = left + sub_len - 1
        if sub_len == 1:
            max_palin[left][right] = 1
        elif sub_len == 2:
            if s[left] == s[right]:
                max_palin[left][right] = 2
            else:
                max_palin[left][right] = 0
        elif s[left] == s[right] and max_palin[left + 1][right - 1] > 0:
            max_palin[left][right] = max_palin[left][left + sub_len // 2 - 1] + 1
        count[max_palin[left][right]] += 1
for i in range(n - 1, 0, -1):
    count[i] += count[i + 1]
for i in range(1, n + 1):
    print(count[i], end=' ')
print()
