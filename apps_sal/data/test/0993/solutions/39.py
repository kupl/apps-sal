from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * (n + 1)

for i in range(n):
    B[i + 1] = B[i] + A[i]  # BはAの累積和

li = [i % m for i in B]  # それをMで割った余りがli

C = Counter(li)  # 余りが同じものの個数が2つ以上ある際、その2つの組み合わせによって、割り切れる和の組み合わせ個数が求まる

ans = 0
for v in C.values():
    if v > 1:
        ans += v * (v - 1) // 2

print(ans)
