arr = []
freq = {}


def exclude(i, n, m):
    s = arr[i]
    for j in range(m):
        if s[j] == '1':
            if freq[j] <= 1:
                return False
    return True


(n, m) = list(map(int, input().split()))
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == '1':
            if j in freq:
                freq[j] += 1
            else:
                freq[j] = 1
    arr.append(s)
ans = False
for i in range(n):
    if exclude(i, n, m):
        ans = True
print('YES' if ans else 'NO')
