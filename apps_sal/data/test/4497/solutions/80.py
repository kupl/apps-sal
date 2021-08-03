import sys
sys.setrecursionlimit(250000)


def main():
    n = int(input())

    if n >= 64:
        print((64))
    elif n >= 32:
        print((32))
    elif n >= 16:
        print((16))
    elif n >= 8:
        print((8))
    elif n >= 4:
        print((4))
    elif n >= 2:
        print((2))
    else:
        print(n)


main()


#
# while True:
#     pair_str = input().split()
#     pair_int = [int(s) for s in pair_str]
#     if pair_int[0] == 0 and pair_int[1] == 0 :
#         break
#     else:
#         input_list.append(pair_int)


# if b > c * 2 :
#     b_price = c
#
# input_array_list = []
#
# while True:
#     input_array = input().split()
#     if input_array[0] == "0" and input_array[1] == "0":
#         break
#     else:
#         input_array_list.append(input_array)
#
# for item in input_array_list:
#     n = int(item[0])
#     k_sum = int(item[1])
#
#     count = 0
#     for i in range(1,n + 1- 2):
#         for j in range(i+1, n + 1 - 1):
#             for k in range (j+1, n+ 1):
#                 if i + j + k == k_sum :
#                     count = count + 1
#     print(count)

#
# for item in input_array_list:
#     if item[1] == "+":
#         print(str(int(item[0])+int(item[2])))
#     elif item[1] =="-":
#         print(str(int(item[0])-int(item[2])))
#     elif item[1] == "/":
#         print(str(int(item[0])//int(item[2])))
#     elif item[1] == "*":
#         print(str(int(item[0])*int(item[2])))
#

# import sympy as sp

# input_list = []
# a,b,c = map(int, input().split())
# divisors = sp.divisors(c)
#
# count = 0
#
# for divisor in divisors:
#     if a <= divisor and divisor <= b:
#         count = count + 1
# print(count)
#
# while True:
#     pair_str = input().split()
#     pair_int = [int(s) for s in pair_str]
#     if pair_int[0] == 0 and pair_int[1] == 0 :
#         break
#     else:
#         input_list.append(pair_int)
#
# for pair_int in input_list:
#     if pair_int[0] <= pair_int[1]:
#         print("{} {}".format(pair_int[0], pair_int[1]))
#     else:
#         print("{} {}".format(pair_int[1], pair_int[0]))

# for i in range(10000):
#    print("Hello World")
#a = input().split()
#a_int = [int(s) for s in a]
#a_sorted = sorted(a_int)
#print(' '.join(map(str, a_sorted)))
