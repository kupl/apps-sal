n = int(input())
m = list(map(int, input().split()))
time = []
products = []
for i in range(len(m)):
    products += [list(map(int, input().split()))]
for i in products:
    time += [15 * len(i) + sum(i) * 5]
print(min(time))
    

