
flag = True
n = int(input())
l = list(map(int, input().split()))

for _ in range(n):
    for num in l:
        if num % 2 == 0:
            if num % 3 == 0 or num % 5 == 0:
                pass
            else:
                flag = False
                break
if flag:
    print("APPROVED")
else:
    print("DENIED")
