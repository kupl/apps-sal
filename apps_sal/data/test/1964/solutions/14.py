n = int(input())
people = list(map(int, input().split()))
goods = []
for i in range(n):
    goods += [list(map(int, input().split()))]
time = []
for j in range(n):
    time += [people[j] * 15 + sum(goods[j]) * 5]
print(min(time))    
