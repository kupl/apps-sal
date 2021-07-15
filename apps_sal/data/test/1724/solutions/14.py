n = int(input())
s = list(map(int, input().split()))
bit = input()
res, m = 0, 0
for i in range(len(bit)):
    if bit[i] == '1':
        res = max(s[i] + res, m)
    m += s[i]
print(res)
