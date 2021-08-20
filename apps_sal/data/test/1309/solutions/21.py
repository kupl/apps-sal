n = int(input())
val = list(map(int, input().split()))
val.sort()
b_a = 10 ** 9
for i in range(len(val) - 1):
    for j in range(i + 1, len(val)):
        if i == j:
            continue
        ans = 0
        (a, b) = (val[i], val[j])
        val.pop(j)
        val.pop(i)
        ans = 0
        for k in range(len(val)):
            if k % 2 == 0:
                ans += abs(val[k + 1] - val[k])
        b_a = min(b_a, ans)
        val.insert(i, a)
        val.insert(j, b)
print(b_a)
