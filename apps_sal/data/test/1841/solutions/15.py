(n, m) = map(int, input().split(' '))
array = input().split(' ')
listx = [int(input()) for inpt in range(m)]
nums = set()
for i in range(n - 1, -1, -1):
    nums.add(array[i])
    array[i] = len(nums)
for a in range(m):
    print(array[listx[a] - 1])
