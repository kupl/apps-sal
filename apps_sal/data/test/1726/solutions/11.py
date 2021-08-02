# your code goes here
n, t = input().split()
n = int(n)
t = int(t)
a = list(map(int, input().split()))
count = 0
sum = 0
for i in a:
    sum = 86400 - i
    t -= sum
    count += 1
    if(t <= 0):
        print(count)
        break
