n = int(input())
a = list(map(int, input().split()))

# oを選択 xを非選択とする　左から見て
# oxoxoxoxoxo に x を1つか2つ挿入することを考える
# 状態を4つ設定 (最後がxかoか)(挿入ずみのxの数)の形式でやる
# a=[1,2,3,4,5,6,7]
# n=len(a)
x0, x1, x2, o0, o1, o2 = a[0], -10**18, 0, -10**18, a[1], -10**18
for i in a[2:]:
    x0, x1, x2, o0, o1, o2 = o0, max(o1, x0), max(o2, x1), x0 + i, x1 + i, x2 + i
if n % 2 == 0:
    print(max(x0, x1, o1))
else:
    print(max(x1, x2, o2))
