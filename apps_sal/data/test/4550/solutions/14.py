# A - キャンディーと2人の子供
# https://atcoder.jp/contests/abc047/tasks/abc047_a

a, b, c = list(map(int, input().split()))

result = 'No'

if a + b == c or a + c == b or a == b + c:
    result = 'Yes'

print(result)

