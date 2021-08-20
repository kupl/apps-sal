N = int(input())
S = input()
ret = 'No'
for i in range(N // 2):
    s = S[:i + 1]
    if s + s == S:
        ret = 'Yes'
        break
print(ret)
