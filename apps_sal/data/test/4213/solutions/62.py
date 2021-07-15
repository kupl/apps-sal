N = int(input())
a_list = list(map(int, input().split()))
max_ = abs(max(a_list) - min(a_list))
print(max_)
