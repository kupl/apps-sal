n = int(input())
lis = list(map(int, input().split()))
a = 0
b = 0
c = 0
output = 0
for i in range(len(lis)):
    a = lis[i]
    for j in range(i + 1, len(lis)):
        b = lis[j]
        for k in range(j + 1, len(lis)):
            c = lis[k]
            if a + b > c and a + c > b and (b + c > a) and (a != b and b != c and (c != a)):
                output += 1
print(output)
