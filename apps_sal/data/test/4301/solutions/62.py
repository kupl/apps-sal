n = int(input())
numbers = []
for i in range(n):
  a = int(input())
  numbers.append(a)
b = max(numbers)
max_index = numbers.index(max(numbers))
numbers.remove(b)
for i in range(n):
  if i == max_index:
    print(max(numbers))
  else:
    print(b)
