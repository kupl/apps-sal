# B - Hina Arare
# https://atcoder.jp/contests/abc089/tasks/abc089_b

N = int(input())
s = list(map(str, input().split()))

result = 'Three'

if s.count('Y') > 0:
    result = 'Four'

print(result)
