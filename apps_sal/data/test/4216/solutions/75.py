n = int(input())
ans = []

for i in range(1, int(n**0.5) + 1):
    if (n / i).is_integer():
        a = len(str(i))
        b = len(str(int(n / i)))
        x = max(a, b)
        ans.append(x)


print(min(ans))
