N = int(input())
int_list = []
for _ in range(N):
  int_list.append(int(input()))
int_list.sort()
print(len(set(int_list)))
