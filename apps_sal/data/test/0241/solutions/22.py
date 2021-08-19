n, m, mn, mx = input().split()
n, m, mn, mx = int(n), int(m), int(mn), int(mx)
diff = n - m
tem = [int(x) for x in input().split()]
flag = 0
check = 0
for x in tem:
    if x == mn or x == mx:
        flag = 1
    if x < mn or x > mx:
        check = 1

# print(flag,diff)
if not check:
    if diff >= 2:
        print("Correct")
    elif diff == 1 and flag:
        print("Correct")
    else:
        print("Incorrect")
else:
    print("Incorrect")
