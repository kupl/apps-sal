n = input().split()
p = input().split()

n = [int(i) for i in n]
p = [int(i) for i in p]
p = sorted(p)

num = n[1]

total = p[0:num]
total_price =sum(total)


print(total_price)
