N = int(input())
S = map(int, input().split())
length_list = list(S)
length_list.sort(reverse=True)
# print(length_list)
max_length = length_list.pop(0)
# print(max_length)

if max_length < sum(length_list):
    print("Yes")
else:
    print("No")
