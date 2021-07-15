n = int(input())
for i in range(n):
    num = int(input())
    lst = list(map(int, input().split()))
    even = 0
    odd = 0
    for j in lst:
        if j % 2 == 0:
            even+=1
        else:
            odd+=1
    if odd == 0 or (odd == num and num % 2 == 0):
        print("NO")
    else:
        print("YES")
