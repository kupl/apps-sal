(n, m) = map(int, input().split())
s = input()
s = ''.join(reversed(s))
ans = []
index = 0
while index < n:
    next_index = -1
    for j in range(min(index + m, n), index, -1):
        if s[j] == '0':
            next_index = j
            break
    if next_index == -1:
        ans = [-1]
        break
    ans.append(next_index - index)
    index = next_index
print(' '.join(list(map(str, list(reversed(ans))))))
