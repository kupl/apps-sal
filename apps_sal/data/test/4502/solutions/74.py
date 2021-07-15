n = int(input())
a_list = [int(x) for x in input().split()]
if n % 2 == 0:
    b_list = a_list[n-1::-2] + a_list[0::2]
else:
    b_list = a_list[n-1::-2] + a_list[1::2]
print(*b_list)
