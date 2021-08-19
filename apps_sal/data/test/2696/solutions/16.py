# cook your dish here
n = int(input())
lis = []
lis = input().split(" ")
pos = n
for i in range(n - 1):
    if(lis[n - 1] == lis[n - i - 2]):
        pos = n - i - 1
    else:
        break
print(pos)
