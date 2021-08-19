n = int(input())
count = 0
say = 'No'
for i in range(n):
    (a, b) = [int(x) for x in input().split()]
    if a == b:
        count += 1
        if count >= 3:
            say = 'Yes'
    else:
        count = 0
print(say)
