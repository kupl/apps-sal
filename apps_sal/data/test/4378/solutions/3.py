n = int(input())
s = [i for i in input()]
T = ['R', 'G', 'B']
add = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        add += 1
        if i + 2 < n:
            for j in T:
                if j != s[i] and j != s[i + 2]:
                    s[i + 1] = j
                    break
        else:
            for j in T:
                if j != s[i]:
                    s[i + 1] = j
                    break
print(add)
print(''.join(s))
