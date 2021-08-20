a = [int(input()) for _ in range(5)]
b = [(i - 1) % 10 + 1 for i in a]
count = sum(((i // 10 + (1 if i % 10 != 0 else 0)) * 10 for i in a))
print(count - (10 - min(b)))
