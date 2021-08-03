n, k, c = map(int, input().split())
s = input()

left = []
i = 0
while len(left) < k:
    if s[i] == 'o':
        left.append(i)
        i += c + 1
    else:
        i += 1

right = []
i = n - 1
while len(right) < k:
    if s[i] == 'o':
        right.append(i)
        i -= c + 1
    else:
        i -= 1

right = right[::-1]

for i in range(k):
    if left[i] == right[i]:
        print(left[i] + 1)
