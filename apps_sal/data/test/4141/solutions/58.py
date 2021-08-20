n = int(input())
nums = list(map(int, input().split()))
evens = [num for num in nums if num % 2 == 0]
approved = all([even % 3 == 0 or even % 5 == 0 for even in evens])
print('APPROVED ' if approved else 'DENIED')
