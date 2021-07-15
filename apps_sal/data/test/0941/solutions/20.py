b, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(len(a)):
    ans += pow(b, k - i - 1, 2) * a[i] % 2
print("odd" if ans % 2 else "even")
