# 異なる二つの組み合わせの最小値を求める

a, b, c = list(map(int, input().split()))

vales = [a + b, a + c, b + c]

print((min(vales)))

