n, k = map(int, input().split())

def IsGoodNumber(number):
  return "0123456789"[:k + 1] in ''.join(sorted(set(number)))

numbers = [input() for _ in range(n)]
print(sum(1 for number in numbers if IsGoodNumber(number)))
