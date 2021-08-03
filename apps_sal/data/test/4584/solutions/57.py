n = int(input())
a = list(map(int, input().split()))
number_buka = [0] * n

for i in a:
    number_buka[i - 1] += 1

for j in number_buka:
    print(j)
