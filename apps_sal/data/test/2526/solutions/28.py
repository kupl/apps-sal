(x, y, a, b, c) = map(int, input().split())
datp = sorted(list(map(int, input().split())), reverse=True)
datq = sorted(list(map(int, input().split())), reverse=True)
datr = list(map(int, input().split()))
dat = sorted(datp[:x] + datq[:y] + datr, reverse=True)
print(sum(dat[:x + y]))
