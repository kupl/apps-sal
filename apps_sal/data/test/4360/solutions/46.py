n = int(input())
a_list = [1 / int(i) for i in input().split()]
ans = 1 / sum(a_list)
print(ans)
