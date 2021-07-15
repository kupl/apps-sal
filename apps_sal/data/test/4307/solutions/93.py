n = int(input())
ans = []

for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0 and i % 2 == 1:
            count += 1
        if count == 8:
            ans.append(i)

print(len(ans))
