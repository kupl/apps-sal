N = int(input())
A = [int(i) for i in input().split()]
for n in A:
    if(n % 2):
        print("First")
        break
else:
    print("Second")
