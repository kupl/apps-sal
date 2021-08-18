s = input()
n = len(s)
ans = 0

for i in range(2 ** (n - 1)):
    k = 0
    num_list = []
    for j in range(n):
        if (i >> j) & 1:
            num = s[k: j + 1]
            k = j + 1
            num_list.append(int(num))
    num = s[k: n + 1]
    num_list.append(int(num))
    ans += sum(num_list)
print(ans)
