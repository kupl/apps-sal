# A - Two Rectangles
# https://atcoder.jp/contests/abc052/tasks/abc052_a

square = list(map(int, input().split()))

result = [square[0] * square[1], square[2] * square[3]]
print((max(result)))
