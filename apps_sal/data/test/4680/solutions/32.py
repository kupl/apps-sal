x = input().split()
fn = 0
sn = 0

for i in range(len(x)):
    if int(x[i]) == 5:
        fn += 1
    elif int(x[i]) == 7:
        sn += 1

if fn == 2:
    if sn == 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
