n = int(input())
ip = list(map(int, input().split()))
count = 0
odd = 0
for i in ip:
    if i % 2 == 1:
        odd = 1
    count += i
if count % 2 == 1:
    print("First")
else:
    if odd == 1:
        print("First")
    else:
        print("Second")
