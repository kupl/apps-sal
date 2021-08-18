N = int(input())
S = map(int, input().split())
length_list = list(S)
length_list.sort(reverse=True)
max_length = length_list.pop(0)

if max_length < sum(length_list):
    print("Yes")
else:
    print("No")
