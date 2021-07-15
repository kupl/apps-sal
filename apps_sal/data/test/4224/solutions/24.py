n = int(input())
a = list(map(int, input().split()))
cnt = 0

for c in a:
  cnt += format(c, 'b')[::-1].find('1')

print(cnt)
