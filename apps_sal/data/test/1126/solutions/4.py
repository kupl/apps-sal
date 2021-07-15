n, x, m = map(int, input().split())
d = [0]*(m+1)
tmp = x
check = [tmp]
while d[tmp] == 0:
    d[tmp] = 1
    tmp = (tmp**2)%m
    check.append(tmp)
for i in range(len(check)):
    if check[i] == check[-1]:
        index = i
        break
sum_c = sum(check[index:len(check)-1])
cycle = (n - index) // (len(check)-index-1)
rest = n - index - cycle*(len(check)-index-1)
print(sum(check[:index+rest])+sum_c*cycle)
