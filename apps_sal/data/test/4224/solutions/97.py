n = int(input())
a = list(map(int, input().split()))
count = 0
for i in a:
    count += len(bin(i)) - bin(i).rfind('1') - 1
print(count)
