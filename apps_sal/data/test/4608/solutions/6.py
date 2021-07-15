n = int(input())
a = [int(input())-1 for _ in range(n)]

visit_node = [0]*(n)
ans = 0
curr_node = 0

while(visit_node[curr_node] == 0):
    visit_node[curr_node] = 1
    curr_node = a[curr_node]
    ans += 1
    if curr_node == 1:
        print(ans)
        return
print(-1)
