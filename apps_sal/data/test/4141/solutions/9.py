n = int(input())
a = list(map(int, input().split()))

for i in a:
    if i % 2 == 0:
        if i % 3 and i % 5 :
            print("DENIED")
            return

print("APPROVED")
