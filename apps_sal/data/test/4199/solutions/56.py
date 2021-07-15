x, y = map(int, input().split())
num_list = [num for num in map(int, input().split()) if num >= y]
print(len(num_list))
