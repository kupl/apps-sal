a, b, c = map(int, input().split())
bell_price = (a, b, c)
print(sum(bell_price) - max(bell_price))
