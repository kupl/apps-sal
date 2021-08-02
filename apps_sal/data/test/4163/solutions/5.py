N = int(input())
count = 0
for i in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        count = count + 1
        if count >= 3:
            print("Yes")
            break
    else:
        count = 0
if(count != 3):
    print("No")
