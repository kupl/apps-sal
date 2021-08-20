N = int(input())
A = list(map(int, input().split()))
evens = [num for num in A if num % 2 == 0]
bool_list = [even % 3 == 0 or even % 5 == 0 for even in evens]
result = all(bool_list)
print('APPROVED' if result else 'DENIED')
