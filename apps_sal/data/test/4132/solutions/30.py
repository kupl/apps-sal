n = int(input())
num_list = list(map(int, input().split()))

while len(num_list) >= 2:
    x = min(num_list)
    num_list = [i % x for i in num_list if (i % x != 0)]
    num_list.append(x)
 
print(num_list[0])
