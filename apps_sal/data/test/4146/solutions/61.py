import collections
n = int(input())
v = list(map(int, input().split()))
even = [v[2 * i] for i in range(n // 2)]
odd = [v[2 * i + 1] for i in range(n // 2)]
dEven = collections.Counter(even).most_common()
dOdd = collections.Counter(odd).most_common()
if dEven[0][0] != dOdd[0][0]:
    ans = n - dEven[0][1] - dOdd[0][1]
elif len(dEven) >= 2 and len(dOdd) >= 2:
    ans = n - max(dEven[0][1] + dOdd[1][1], dEven[1][1] + dOdd[0][1])
elif len(dEven) < len(dOdd):
    ans = n - (dEven[0][1] + dOdd[1][1])
elif len(dEven) > len(dOdd):
    ans = n - (dEven[1][1] + dOdd[0][1])
else:
    ans = n // 2
print(ans)
