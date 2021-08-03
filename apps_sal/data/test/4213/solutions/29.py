n = int(input())
a = list(map(int, input().split()))
num_list = list(a)

answer = (max(num_list) - min(num_list))

print(answer)
