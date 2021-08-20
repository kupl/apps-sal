n = int(input())
a_list = [int(x) for x in input().split()]
print(*a_list[n - 1::-2] + a_list[n % 2::2])
