n = int(input())
a = list(map(int, input().split()))
difficulty = a[0]
expectation = a[0] % 998244353
for i in range(1, n):
    expectation = expectation * 2 + difficulty + a[i]
    difficulty = difficulty * 2 + a[i]
    expectation %= 998244353
    difficulty %= 998244353
print(expectation)
