# 入力値が1~Nの整数である前提があって成り立つ
# ↓は公式の解答例的なの
n, k = map(int, input().split())
print((n - 1 + k - 2) // (k - 1))
