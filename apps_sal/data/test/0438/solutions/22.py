#not submitted not completed
#http://codeforces.com/problemset/problem/753/A
n = int(input())
sum = 0
numbers = []
i = 1
while sum < n:
	numbers.append(i)
	sum += i
	i += 1
if sum > n:
	del numbers[sum - n - 1]
print(len(numbers))
for j in numbers:
	print(j, end=" ")
print()
