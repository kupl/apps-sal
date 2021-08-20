n = int(input())
x = [int(i) for i in input().split()]
odd = 0
even = 0
for i in x:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(min([odd, even]))
