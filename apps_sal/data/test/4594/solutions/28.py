N = int(input())
num_list = []
for n in range(N):
    num = int(input())
    num_list.append(num)
ans = len(set(num_list))
print(ans)
