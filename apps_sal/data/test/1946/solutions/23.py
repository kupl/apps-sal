a_size = int(input())
elements = {}
for _ in range(a_size):
    index, price = map(int, input().split())
    elements[index] = price

b_size = int(input())
for _ in range(b_size):
    index, price = map(int, input().split())
    elements[index] = max(price, elements.get(index, 0))

print(sum(elements.values()))
