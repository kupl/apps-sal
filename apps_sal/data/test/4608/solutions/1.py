n = int(input())
a = [int(input()) - 1 for _ in range(n)]
curr_node = 0
for i in range(n):
    curr_node = a[curr_node]
    if curr_node == 1:
        print(i + 1)
        return
print(-1)
