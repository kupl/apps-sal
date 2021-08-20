(a, b, k) = list(map(int, input().split()))
mylist = []
c = min(a, b)
for i in range(1, c + 1):
    if a % i == 0 and b % i == 0:
        mylist.append(i)
print(mylist[-k])
