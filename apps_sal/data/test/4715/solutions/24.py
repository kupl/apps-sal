abc = list(map(int, input().split()))
count = 0
for i in range(0, len(abc) - 1):
    abc.sort()
    if(abc[i] != abc[i + 1]):
        count += 1


print(count + 1)
