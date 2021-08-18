n = int(input())
lst = list(map(int, input().split()))
lst = lst + lst
count = 0
large = 0
for i in lst:
    if i == 1:
        count += 1
    else:
        if count > large:
            large = count
        count = 0
print(large)
